function toggleText() {

						// Get all the elements from the page
						var text = document.getElementById("moreText");

            var buttonText = document.getElementById("textButton");

            // If the display property of the dots
            // to be displayed is already set to
            // 'none' (that is hidden) then this
            // section of code triggers
            if ( !(text.style.display === "none") ) {

                // Hide the text between the span elements
                text.style.display = "none";

                // Change the text on button to
                // 'Show More'
                buttonText.innerHTML = "Show More";
            }

            // If the hidden portion is revealed,
            // we will change it back to be hidden
            else {

                // Show the text between the
                // span elements
                text.style.display = "inline";

                // Change the text on button
                // to 'Show Less'
                buttonText.innerHTML = "Show Less";
							}
}

Footer
