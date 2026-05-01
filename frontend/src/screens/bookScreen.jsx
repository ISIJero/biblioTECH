import React, { useState, useEffect } from "react";
// import { Table, Button, Card } from "react-bootstrap";
import styles from "./bookScreen.module.css";
import { TableComponent } from "../components/tableComponent.jsx";

export function BookScreen() {
  return (
    <div className={styles.container}>
      <div className={styles.buttonContainer}>
        <button>Agregar Libros</button>
        <button>Modificar Libro</button>
        <button>Eliminar Libro</button>
      </div>
      <div className={styles.tableContainer}>
        <TableComponent />
      </div>
    </div>
  );
}
