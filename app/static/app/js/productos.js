const targetDiv = document.getElementById("third");
const btn = document.getElementById("esconder");
btn.onclick = function () {
    if (targetDiv.style.display !== "none") {
    targetDiv.style.display = "none";
    } else {
    targetDiv.style.display = "block";
    }
};

// VALIDACION DE FORMULARIO CON BOOTSTRAP
// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()

/* BOTON ELIMINAR */

function confirmarEliminar(id){ 
  swal.fire({
      title: '¿Estás seguro?',
      text: "El producto será eliminado de la base de datos",
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
          text: 'El producto ha sido eliminado de la base de datos',
          icon: 'success',
          showConfirmButton: false,
          allowOutsideClick: false
      })
          window.location.href = "/eliminarproducto/"+id+"/";

      } else if (
      /* Read more about handling dismissals below */
      result.dismiss === Swal.DismissReason.cancel
      ) {
      swal.fire({
          title: 'Cancelado',
          text: 'El producto no ha sido eliminado',
          icon: 'error',
          confirmButtonColor: '#4CAF50'
      })
      }
  })
}

