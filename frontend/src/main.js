const { app, BrowserWindow, Menu, session, screen } = require("electron");
const path = require("node:path");
const { spawn } = require("child_process");
const { cwd } = require("node:process");

let pythonProcess = null;
const backendDir = path.join(__dirname, "..", "..", "..", "backend");

function startBackend() {
  console.log(backendDir);
  pythonProcess = spawn(
    "python3",
    [
      "-m",
      "uvicorn",
      "main:app",
      "--host",
      "127.0.0.1",
      "--port",
      "8000",
      "--reload",
    ],
    { cwd: backendDir },
  );
  pythonProcess.stdout.on("data", (data) => {
    console.log(`Backend: ${data}`);
  });
  pythonProcess.stderr.on("data", (data) => {
    console.error(`Backend Error: ${data}`);
  });
}

// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require("electron-squirrel-startup")) {
  app.quit();
}

const createWindow = () => {
  const primaryDisplay = screen.getPrimaryDisplay();
  const { width, height } = primaryDisplay.workAreaSize;
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    title: "biblioTECH",
    width,
    height,
    webPreferences: {
      preload: MAIN_WINDOW_PRELOAD_WEBPACK_ENTRY,
      webSecurity: false,
    },
  });

  session.defaultSession.webRequest.onHeadersReceived((details, callback) => {
    callback({
      responseHeaders: {
        ...details.responseHeaders,
        "Content-Security-Policy": [
          "default-src 'self' 'unsafe-inline' 'unsafe-eval' data:; connect-src 'self' http://127.0.0.1:8000 ws://localhost:3000 http://localhost:3000;",
        ],
      },
    });
  });

  // and load the index.html of the app.
  mainWindow.loadURL(MAIN_WINDOW_WEBPACK_ENTRY);

  // Open the DevTools.
  mainWindow.webContents.openDevTools();
};

Menu.setApplicationMenu(null);

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  startBackend();
  createWindow();

  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    if (pythonProcess) pythonProcess.kill();
    app.quit();
  }
});

app.on("will-quit", () => {
  if (pythonProcess) pythonProcess.kill();
});
// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.
