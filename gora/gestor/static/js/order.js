var orders = 0

$( document ).ready(function() {
    orders++;
    $('#table-add tbody').append(html())
});

function html(id){
    var html = '<tr><th id="item-$id"><input class="order-add-input"type="number" name="qty-$id" step="1" min="1"></th><td>'
    html += html_radios()
    html += '</td><td class="text-center"><span  id="borrar-$id" class="badge badge-danger order-edit-label py-1 px-2 mr-2">Borrar</span><span id="agregar-$id" class="badge badge-success order-edit-label py-1 px-2">Agregar</span></td></tr>'
    
    html = html.replace("$id", id)
    return html
}

function html_radios(){
    var html = '<div class="form-row align-items-center"><div class="col"><div class="custom-control custom-radio">'
    html += '<input type="radio" class="custom-control-input" id="salad-$id" name="order-type-$id"><label class="custom-control-label" for="salad-$id">Salad</label></div></div>'
    html += '<div class="col"><div class="custom-control custom-radio"><input type="radio" class="custom-control-input" id="balance-$id" name="order-type-$id"><label class="custom-control-label" for="balance-$id">Balance</label></div></div>'
    html += '<div class="col"><div class="custom-control custom-radio"><input type="radio" class="custom-control-input" id="temping-$id" name="order-type-$id"><label class="custom-control-label" for="temping-$id">Temping</label></div></div></div>'
    return html
}