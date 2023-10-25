// ajax function
// $('.plus-cart').click(function(){
//     console.log("button clicked")
// })

$('.plus-cart').click(function(){
    var id =$(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log("pid =" ,id)
    $.ajax({
        type :'GET',
        url : '/pluscart/',
        data:(
            prod_id=id
        ),
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
            
    })
})

$('.minus-cart').click(function(){
    var id =$(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    // console.log("pid =" ,id)
    $,ajax({
        type :'GET',
        url: '/minuscart',
        data:(
            prod_id=id
        ),
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
            
    })
})

$('.remove-cart').click(function(){
    var id =$(this).attr("pid").toString();
    var eml = this
    // console.log("pid =" ,id)
    $,ajax({
        type :'GET',
        url : '/removecart',
        data:(
            prod_id=id
        ),
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
            
    })
})






$(document).ready(function () {
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        
        var qty = $(this).closest('.my-3').find('.input-qty').val();
        var value = parseInt(qty,10);
        value = isNaN(value) ? 0 : value;
        if(value <10)
        {
            value ++;
           
            $(this).closest('.my-3').find('.input-qty').val(value);
        } 
    });


    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        
        var qty = $(this).closest('.my-3').find('.input-qty').val();
        var value = parseInt(qty,10);
        value = isNaN(value) ? 0 : value;
        if(value > 0)
        {
            value--;
           
            $(this).closest('.my-3').find('.input-qty').val(value);
        }

        
    });
    
    
       
    
});