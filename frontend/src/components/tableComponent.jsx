import React, { useEffect, useState } from "react";

export function TableComponent() {
  const [books, setBooks] = useState([]);

  const getBooks = () => {
    fetch("http://127.0.0.1:8000/books/")
      .then((response) => response.json())
      .then((data) => setBooks(data));
  };

  useEffect(() => {
    getBooks();
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>TITULO</th>
          <th>AUTOR</th>
          <th>MATERIA</th>
          <th>ISBN</th>
          <th>CÓDIGO</th>
          <th>ESTADO</th>
        </tr>
      </thead>
      <tbody>
        {books.map((book) => (
          <tr key={book.id}>
            <td>{book.nombre}</td>
            <td>{book.autor}</td>
            <td>{book.materia}</td>
            <td>{book.isbn}</td>
            <td>{book.cod}</td>
            <td>{book.estado}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
