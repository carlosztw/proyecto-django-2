class usuario{
    rut;
    nombre;
    apellido;
    fecha;
    correo;
    contrasena;
    numero;
    direccion;
    //mutadores
    setRut(rut){
        this.rut=rut;
    }
    setNombre(nombre){this.nombre=nombre;}
    setApellido(apellido){this.apellido=apellido;}
    setFecha(fecha){this.fecha=fecha;}
    setCorreo(correo){this.correo+correo;}
    setContrasena(contrasena){this.contrasena=contrasena;}
    setnumero(numero){this.numero;}
    setdireccion(direccion){this.direccion;}

    /////////////////
    getRut(){
        return this.rut;
    }
    getNombre(){return this.nombre;}
    getApellido(){return this.apellido;}
    getFecha(){return this.fecha;}
    getCorreo(){return this.correo;}
    getContrasena(){return this.contrasena;}
    getNumero(){return this.numero;}
    getDireccion(){return this.direccion;}

    imprimir(){
        return ' nombre:' +this.getNombre()+' Apellido:'+this.getApellido()+ 
        ' rut:'+this.getRut()+' Fecha:' +this.getFecha()+ ' Correo: '+this.getCorreo()+
        ' contrasena: '+this.getContrasena()+' Numero: '+this.getNumero()+' Direccion:'+this.getDireccion; 
    }


}