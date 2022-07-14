function sumar(){
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'Unidad agregada al carro',
        showConfirmButton: false,
        timer: 1500,
        width: '350px'
    })
}

function restar(){
    Swal.fire({
        position: 'top-end',
        icon: 'info',
        title: 'Unidad restada del carro',
        showConfirmButton: false,
        timer: 1500,
        width: '350px'
    })
}

function limpiar(){
    Swal.fire({
        position: 'top-end',
        icon: 'info',
        title: 'Productos eliminados del carro',
        showConfirmButton: false,
        timer: 1500,
        width: '350px'
    })
}