function AlbumViewModel() {
	var self = this;
	self.listado = ko.observableArray([]);
	self.mensaje = ko.observable('');

	self.albumVO = {
		id: ko.observable(0),
		nombre: ko.observable('').extend({ required: { message: ' Digite el nombre del album.' } }),
		caratula: ko.observable('').extend({ required: { message: ' Debe cargar la imagen de la caratula.' } }),
		artista_id: ko.observable(0).extend({ required: { message: ' Seleccione el artista.' } })
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
			 	if (success == 'ok' && datos.data!=null && datos.data.length > 0) {
			 		self.mensaje('');
			 		self.listado(datos.data);
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
}
var album = new AlbumViewModel();