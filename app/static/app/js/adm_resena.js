/* BOTON ELIMINAR */

function confirmarEliminar(id){ 
    swal.fire({
        title: '¿Estás seguro?',
        text: "La reseña será eliminada de la base de datos",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#4CAF50',
        cancelButtonColor: '#f44336' ,
        confirmButtonText: 'Sí',
        cancelButtonText: 'No',
        reverseButtons: true,
        allowOutsideClick: false
    }).then((result) => {
        if (result.isConfirmed) {
        swal.fire({
            title: '¡Eliminado!',
            text: 'La reseña ha sido eliminada de la base de datos',
            icon: 'success',
            allowOutsideClick: false,
            confirmButtonColor: '#4CAF50'
          }).then(function() {
              window.location.href = "/eliminarresena/"+id+"/";
          })
  
        } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
        ) {
        swal.fire({
            title: 'Cancelado',
            text: 'La reseña no ha sido eliminada',
            icon: 'error',
            confirmButtonColor: '#4CAF50'
        })
        }
    })
  }