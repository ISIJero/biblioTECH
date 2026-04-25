import React, { useState, useEffect } from "react";
// import { Table, Button, Card } from "react-bootstrap";
import styles from "./bookScreen.module.css";

export function BookScreen() {
  /*  const [books, setBooks] = useState([]);

  const get_books = () => {
    fetch("http://127.0.0.1:8000/books/")
      .then((response) => response.json())
      .then((data) => setBooks(data));
  };

  useEffect(() => {
    get_books();
  }, []); */

  return (
    <div className={styles.container}>
      <div className={styles.buttonContainer}>
        <button>Agregar Libros</button>
        <button>Modificar Libro</button>
        <button>Eliminar Libro</button>
      </div>
      <div className={styles.tableContainer}>
        <table>
          <thead>
            <tr>
              <th>TITULO</th>
              <th>MATERIA</th>
              <th>CÓDIGO</th>
              <th>AUTOR</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Matemática 2</td>
              <td>Matemáticas</td>
              <td>789546123</td>
              <td>Steward</td>
            </tr>
            <tr>
              <td>Física</td>
              <td>Cs. Naturales</td>
              <td>456123789</td>
              <td>Sear Semanzky</td>
            </tr>
            <tr>
              <td>El Cuerpo Humano</td>
              <td>Cs. Naturales</td>
              <td>7891596324</td>
              <td>Brown</td>
            </tr>
            <tr>
              <td>La Batalla de Caseros</td>
              <td>Cs. Sociales</td>
              <td>43554981</td>
              <td>Pereira</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
