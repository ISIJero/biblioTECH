from schemas.member import Member, MemberIn
from config.db_connection import DataBaseManagment
from typing import List
from fastapi import HTTPException

dbm = DataBaseManagment()


def get_all_members() -> List[Member]:
    query = """SELECT * FROM personas"""
    data = list()

    with dbm:
        rows = dbm.extract_data(query=query)

        for row in rows:
            data.append(dict(row))

    return data


def get_member_by_id(id: int) -> Member:
    query = """SELECT * FROM personas WHERE id = :id"""
    data = list()

    with dbm:
        rows = dbm.extract_data(query=query, param={"id": id})

        for row in rows:
            data.append(dict(row))

    return data[0]


def add_member(member: MemberIn) -> Member:
    query = """
    INSERT INTO personas (nombre, curso, rol) 
    VALUES (:nombre, :curso, :rol)"""

    with dbm:
        last_record_id = dbm.execute_query(query=query, param=member.model_dump())

    return {**member.model_dump(), "id": last_record_id.lastrowid}


def update_member(id: int, member: MemberIn) -> Member:
    query = """
    UPDATE personas
    SET nombre=:nombre,
        curso=:curso,
        rol=:rol
    WHERE id=:id"""
    param = {"id": id, **member.model_dump()}

    with dbm:
        dbm.execute_query(query=query, param=param)

    return {"id": id, **member.model_dump()}


def delete_member(id: int) -> dict:
    query = """DELETE FROM personas WHERE id=:id"""

    with dbm:
        result = dbm.execute_query(query=query, param={"id": id})
        if not result.rowcount:
            raise HTTPException(status_code=404, detail="Persona no encontrada")

    return {"Result": "Libro borrado exitósamente"}


if __name__ == "__main__":
    pass
