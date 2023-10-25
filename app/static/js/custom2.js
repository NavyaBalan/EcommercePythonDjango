


// $(document).ready(function () {



    // Plus button click event

    $(".plus-cart").on("click", function (e) {
        e.preventDefault();
        var productId = $(this).attr("id");
        var eml = this.parentNode.children[2];
        
        $.ajax({
            type: "GET",
            url: "/pluscart/", 
            data: { prod_id: productId },
            success: function (data) {
                // document.getElementById("quantity").innerText = data.quantity;
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data. amount;
                document.getElementById("totalamount").innerText = data.totalamount;
               
            },
        });
    });

    // Minus button click event
    
    $(".minus-cart").on("click", function (e) {
        e.preventDefault();
        var productId = $(this).attr("id");
        var eml = this.parentNode.children[2];
        $.ajax({
            type: "GET",
            url: "/minuscart/", 
            data: { prod_id: productId },
            success: function (data) {
                // document.getElementById("quantity").innerText = data.quantity;
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
            },
        });
    });





    // Remove button click event
    $(".remove-cart").on("click", function (e) {
        e.preventDefault();
        var productId = $(this).attr("pid");
        var eml = this
        $.ajax({
            type: "GET",
            url: "/removecart/", 
            data: { prod_id: productId },
            success: function (data) {

                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
                eml.parentNode.parentNode.parentNode.remove()
                
            },
        });
    });
// });






