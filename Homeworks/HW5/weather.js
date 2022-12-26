function toCelsius(){

	// grabs the input from the user
	let input =  document.getElementById("temperature").value;

	// converts the temperature to C
	let celsius = (input - 32) * 5/9;

	// chcek if input is value
	if(isNaN(celsius)){


		document.getElementById("result-parent").style.fontWeight = "bold";
		document.getElementById("result-parent").style.color = "red"
		document.getElementById("result-parent").style.visibility = "visible";

		document.getElementById("result-parent").innerText = "Please input a valid number!";



	}else{

		// makes the div visible
		// element.style can be used to change CSS properties of an HTML document
		document.getElementById("result-parent").style.color = "black";
		document.getElementById("result-parent").style.fontWeight = "normal";
		document.getElementById("result-parent").style.visibility = "visible";

		// show back to the user 
		document.getElementById("result-parent").innerText = "The Temperature in Celsius is " + celsius;



	}

}
Footer
