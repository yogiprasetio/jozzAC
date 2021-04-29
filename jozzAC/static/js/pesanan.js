$('.klik').click(function(){
		var appr = $(this).data('approve');
		

		document.getElementById("nama").innerHTML = "Nama Client : " + $(this).data('nama');
		document.getElementById("kwitansi").innerHTML = $(this).data('kwitansi');
		document.getElementById("kota").innerHTML = "Kota " + $(this).data('kota');
		document.getElementById("telp").innerHTML = "No Telp Client : " + $(this).data('telp');
		document.getElementById("alamat").innerHTML = "Alamat : " + $(this).data('alamat');
		document.getElementById("ket").innerHTML = $(this).data('ket');
		
	// 	var socket = new WebSocket(`ws://127.0.0.1:8000/ws/pesanan/${$(this).data('id')}/`)
	// 	socket.onmessage = function(event){
	// 		var data = JSON.parse(event.data);
	// 		console.log(data);
	// }
});