import "bootstrap/dist/css/bootstrap.min.css";
import * as React from "react";
import { createRoot } from "react-dom/client";
import { HashRouter as Router, Routes, Route, Link } from "react-router-dom";
import { BookScreen } from "./screens/bookScreen.jsx";
import style from "./app.module.css";

// Buscamos el div contenedor
const container = document.getElementById("root");
const root = createRoot(container);

// Creamos un componente principal de prueba
function App() {
  return (
    <Router>
      <div className={style.container}>
        <div className={style.optionSide}>
          <h3>biblioTECH</h3>
          <div className={style.buttonPanel}>
            <a href="#">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="icon icon-tabler icons-tabler-outline icon-tabler-notebook"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                  <path d="M6 4h11a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-11a1 1 0 0 1 -1 -1v-14a1 1 0 0 1 1 -1m3 0v18" />
                  <path d="M13 8l2 0" />
                  <path d="M13 12l2 0" />
                </svg>
                Libros
              </span>
            </a>
            <a href="#">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="icon icon-tabler icons-tabler-outline icon-tabler-user"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                  <path d="M8 7a4 4 0 1 0 8 0a4 4 0 0 0 -8 0" />
                  <path d="M6 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2" />
                </svg>
                Personas
              </span>
            </a>
            <a href="#">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="icon icon-tabler icons-tabler-outline icon-tabler-transfer"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                  <path d="M20 10h-16l5.5 -6" />
                  <path d="M4 14h16l-5.5 6" />
                </svg>
                Préstamos
              </span>
            </a>
          </div>
        </div>
        <Routes>
          <Route path="/" element={<BookScreen />} />
        </Routes>
      </div>
    </Router>
  );
}

// Renderizamos el componente dentro del root
root.render(<App />);
