function split( val ) {
    return val.split( /,\s*/ );
}
function extractLast( term ) {
    return split( term ).pop();
}
function installTaggingAutocompleate(id, api_url){
	$("#" + id).autocomplete({
		source: function(request, response){
			$.getJSON(api_url, {
				term: extractLast(request.term)
			}, response);
		},
		search: function(){
			// custom minLength
			var term = extractLast(this.value);
			if (term.length < 2) {
				return false;
			}
		},
		focus: function(){
			// prevent value inserted on focus
			return false;
		},
		select: function(event, ui){
			var terms = split(this.value);
			// remove the current input
			terms.pop();
			// add the selected item
			terms.push(ui.item.value);
			// add placeholder to get the comma-and-space at the end
			terms.push("");
			this.value = terms.join(", ");
			return false;
		}
	});
}