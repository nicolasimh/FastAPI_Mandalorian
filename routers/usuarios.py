from fastapi import APIRouter, status
from models.usuario import Usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["usuario"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
)


@router.get("/", status_code=status.HTTP_200_OK)
async def getUsuario():
    return "Hola soy un usuario de Mandalorian"


@router.get("/nombre", status_code=status.HTTP_200_OK)
async def getUsuarioNombre(usuario: Usuario):
    return "Hola soy un usuario de Mandalorian {}".format(usuario.nombre)



@router.get("/creado/{id}", status_code=status.HTTP_200_OK)
async def getUsuario(id: int):
    return "Hola soy un usuario de Mandalorian creado id: {}".format(id)

