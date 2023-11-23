from fastapi import APIRouter

router = APIRouter()


@router.post("/logout")
async def logout():
    return ...
