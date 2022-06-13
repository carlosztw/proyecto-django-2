function mensaje() {
    var nombre = document.getElementById('txtNombre').value;
    alert('Yo soy :' + nombre);
}
function validaForm(){
    var resp = validarut();
    if (resp == false) {
        return false;
    }
    resp = validaFecha();
        if (resp==false){
            return false;
        }
        resp = validaNombre();
    if (resp== false) {
        return false;
    }
    return true;

    }
    

function validaFecha() {
    var fechaUsuario = document.getElementById('txtFechaNaci').value;
    console.log('Fecha de usuario: '+fechaUsuario);
    var fechaSistema = new Date();
    console.log('Fecha sistema: '+ fechaSistema);
    //////////////////
    var ano = fechaUsuario.slice(0,4);
    var mes = fechaUsuario.slice(5,7);
    var dia = fechaUsuario.slice(8,10);
    console.log('Año: '+ano+ 'Mes:' +mes+ 'Dia:' +dia);
    ////////////////////////////////////////////////////
    var fechaNuevaUsuario = new Date(ano,(mes-1),dia);
    console.log('Nueva Fecha Usuario:'+fechaNuevaUsuario);
    if (fechaNuevaUsuario>=fechaSistema) {
        alert('Fecha incorrecta');
        return false;
    }
    /////////////////////////
    var unDia = 24 * 60 * 60 * 1000;///cuantos mili segundos es un dia
    var diferencia_dias =Math.trunc((fechaSistema.getTime() - fechaNuevaUsuario.getTime()) /unDia);
    console.log('Dias: '+diferencia_dias);
    var anos =Math.trunc( diferencia_dias / 365);
    console.log('Años:'+anos);
    if(anos<18){
        alert('usted es menor de edad: '+anos+ 'años de edad');
        return false;
    }
    return true;
}
////////////////////////////////////////// funciones de validacion



function validaNombre() {
    var nombre = document.getElementById('txtNombre').value;
    if(nombre.trim().length < 3){
        alert('El nombre debe de tener un minimo de 3 caracteres');
        return false;
    }
    return true;
}


