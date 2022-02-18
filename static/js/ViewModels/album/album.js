function AlbumViewModel() {
	var self = this;
	self.listado = ko.observableArray([]);
	self.mensaje = ko.observable('');

	self.listadoDeArtistas = ko.observableArray([]);

	self.albumVO = {
		id: ko.observable(0),
		name: ko.observable('').extend({ required: { message: ' Digite el nombre del album.' } }),
		cover: ko.observable('').extend({ required: { message: ' Debe cargar la imagen de la caratula.' } }),
		artist_id: ko.observable(0).extend({ required: { message: ' Debe Seleccionar el artista.' } })
	}

	self.consultarArtistas = function(){
		//if (pagina > 0) {
			path = path_principal + '/api/artist/?format=json&sinpaginacion=1';
			RequestGet(function (datos, success, mensage) {
			 	if (success == 'success' && datos!=null && datos.length > 0) {
			 		self.mensaje('');
			 		self.listadoDeArtistas(agregarOpcionesObservable(datos));

			 	} else {
			 		self.listadoDeArtistas([]);
			 		//self.mensaje(mensajeNoFound);
			 		cerrarLoading()
			 	}
			 	//self.llenar_paginacion(datos,pagina);
			 	cerrarLoading();

			},path, parameter,undefined, false);
		//}
		
	}

	self.consultar = function(pagina){
		if (pagina > 0) {
			path = path_principal + '/api/album/?format=json';
			if (pagina == 1){
				parameter = {
					dato: $('#txtBuscar').val()
				}
			}else{
				parameter = {
					dato: $('#txtBuscar').val(),
					offset: pagina
				}
			}
			RequestGet(function (datos, success, mensage) {
			 	if (success == 'success' && datos!=null && datos.length > 0) {
			 		self.mensaje('');
			 		self.listado(agregarOpcionesObservable(datos));

			 	} else {
			 		self.listado([]);
			 		self.mensaje(mensajeNoFound);
			 		cerrarLoading()
			 	}
			 	//self.llenar_paginacion(datos,pagina);
			 	cerrarLoading();

			},path, parameter,undefined, false);
		}
		
	}

	self.consultar_boton = function(){
		self.consultar(1);
	}


	self.consulta_enter = function(d,e){
		if (e.which == 13) {
            self.consultar_boton();
		}
		return true;
	}

	self.abrir_modal = function(){
		//alert('nuevo album....');
		$('#newAlbumModal').modal('show');
		self.consultarArtistas();
	}

	self.guardarAlbum = function(){
		
		if (AlbumViewModel.errores_album().length == 0) {
			if (self.albumVO.id() == 0) {
				var parametros={
					callback:function(datos, success, mensaje){

						if (success=='success') {
							self.limpiar();
							$('#newAlbumModal').modal('hide');
							self.consultar(1);
						}else{
							 mensajeError(mensaje);
						}
					}, //funcion para recibir la respuesta 
					url:path_principal+'/api/album/',//url api
					parametros:self.albumVO,
					alerta:true,
					metodo: 'POST'
				};
				RequestFormData(parametros);
			}else{

			}
		}else{
			AlbumViewModel.errores_album.showAllMessages();
		}
	}

	self.limpiar = function(){
		self.albumVO.id(0);
		self.albumVO.name('');
		self.albumVO.cover('');
		self.albumVO.artist_id('');
	}

	self.ver_detalle = function(id){
		alert('ver album ' + id);
	}
}

var album = new AlbumViewModel();
AlbumViewModel.errores_album = ko.validation.group(album.albumVO);
ko.applyBindings(album);
