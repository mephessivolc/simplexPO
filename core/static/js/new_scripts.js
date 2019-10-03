// <script language="javascript">
	var input = 1;
	var var_x = 0;
	var count_restri = 0;

	function objetiva(campo) {
		document.getElementById("aqui").innerHTML+="<div><h2>Maximização </h2> </div> <br> z= ";
	   	var i;

	   	if (campo != 0){
	   		for (i=1; i<=campo; i++) {
   		   		if (i == campo){
   		   			document.getElementById("aqui").innerHTML+="<input type='text' value='' id='x"+i+"'> x"+i;
   		      		document.form.campo.value="";
   		      		input++;
   		   		}else{
   		   			document.getElementById("aqui").innerHTML+="<input type='text' value='' id='x"+i+"'> x"+i+ "+ ";
   		      		document.form.campo.value="";
   		      		input++;
   		   		}
	   		}
	   	}
	   	var_x = campo;
	    count_restri = 1;
	    document.getElementById("aqui").innerHTML+="<div><h2>Sujeito a </h2> </div>";
	    mais(campo);
	    mudarestado('label1');
	    mudarestado('campo');
	    mudarestado('definir');
	    mudarestado('add');
	    mudarestado('calcular');
	}

	function mais(campo) {
		var i;


	   	if(count_restri){
	   		for (i=1; i<=campo; i++) {
   		   		if (i == campo){
   		   			document.getElementById("aqui").innerHTML+="<input type='text' value='' id='x"+i+"'> x"+i +
                    "<select><option value='>='>>=</option><option value='<='><=</option><option value='='>=</option></select>" +
                    "<input type='text' value='' id='b"+i+"'><br>";
   		      		document.form.campo.value="";
   		      		input++;
   		   		}else{
   		   			document.getElementById("aqui").innerHTML+="<input type='text' value='' id='b"+i+"'> x"+i+ "+ ";
   		      		document.form.campo.value="";
   		      		input++;
   		   		}
	   		}
	   	}
	}

	function mudarestado(el) {
        var display = document.getElementById(el).style.display;
        if(display == "none")
            document.getElementById(el).style.display = 'block';
        else
            document.getElementById(el).style.display = 'none';
    }
// </script>
