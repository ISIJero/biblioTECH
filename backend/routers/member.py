import services.member as services
from fastapi import APIRouter
from schemas.member import Member, MemberIn
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Member])
def read_members():
    return services.get_all_members()


@router.get("/{id}", response_model=Member)
def read_members_by_id(id: int):
    return services.get_member_by_id(id)


@router.post("/", response_model=Member)
def add_members(member: MemberIn):
    return services.add_member(member)


@router.put("/{id}", response_model=Member)
def update_member(id: int, member: MemberIn):
    return services.update_member(id, member)


@router.delete("/{id}")
def delete_member(id: int):
    return delete_member(id)
