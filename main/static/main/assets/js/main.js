/*
 * Change Navbar color while scrolling
*/

$(window).scroll(function(){
	handleTopNavAnimation();
});

$(window).load(function(){
	handleTopNavAnimation();
});

function handleTopNavAnimation() {
	var top=$(window).scrollTop();

	if(top>10){
		$('#site-nav').addClass('navbar-solid'); 
	}
	else{
		$('#site-nav').removeClass('navbar-solid'); 
	}
}

/*
 * Registration Form
*/

$('#registration-form').submit(function(e)
{
    e.preventDefault();
    
    var postForm = { //Fetch form data
            'confirmData'     : $('#registration-form #confirmData').val(),
            'recordId'     : $('#registration-form #recordId').val(),
            'name'     : $('#registration-form #name').val(),
            'lname'     : $('#registration-form #lname').val(),
            'email'     : $('#registration-form #email').val(),
            'cell'      : $('#registration-form #cell').val(),
            'phone'      : $('#registration-form #phone').val(),
            'address'   : $('#registration-form #address').val(),
            'zipCode'       : $('#registration-form #zipCode').val(),
            'city'      : $('#registration-form #city').val(),
            'country'      : $('#registration-form #country').val(),
            'nif'      : $('#registration-form #nif').val(),
            'modalidade'      : $('#registration-form #modalidade').val(),
            'modPag'      : $('#registration-form #modPag').val(),
            'remarks'      : $('#registration-form #remarks').val(),
            //'program'   : $('#registration-form #program').val(),

            'f2fname'     : $('#registration-form #f2fname').val(),
            'f2email'     : $('#registration-form #f2email').val(),
            'f2cell'      : $('#registration-form #f2cell').val(),
            'f2phone'      : $('#registration-form #f2phone').val(),
            'f2address'   : $('#registration-form #f2address').val(),
            'f2zip'       : $('#registration-form #f2zip').val(),
            'f2city'      : $('#registration-form #f2city').val(),
            'f2country'      : $('#registration-form #f2country').val(),
            'f2nif'      : $('#registration-form #f2nif').val(),

            'csrfmiddlewaretoken'   : $('#registration-form input[name="csrfmiddlewaretoken"]').val()
    };

	//url       : './assets/php/contact.php',
    //dataType  : 'json',
    $.ajax({
            type      : 'POST',
            url       : '/registrationForm',
            data      : postForm,
            dataType  : 'json',
            
            success   : function(data) 
                        {
                            if (data.msg == "Success") 
                            {
                                $('#registration-form #recordId').val(data.recId)
                                /*
                                $('#registration-msg .alert').html("Registration Successful");
                                $('#registration-msg .alert').removeClass("alert-danger");
                                $('#registration-msg .alert').addClass("alert-success");
                                */
                                $('#registration-msg .alert').html("Informação validada com sucesso!");
                                $('#registration-msg .alert').removeClass("alert-danger");
                                $('#registration-msg .alert').removeClass("alert-success");
                                $('#registration-msg .alert').addClass("alert-success");
                                $('#registration-msg').show();

                                $('#registration-submit-btn').hide();
                                $('span#continueToPay').show();
                                $('#change-btn').show();

                                $('select').prop('disabled', true);
                                $('input').prop('disabled', true);
                                $('select#os0').prop('disabled', false);
                                $('.pay').prop('disabled', false);

                                $("button#invoice_other_data").hide();
                                $("span#invoiceOther_Msg").hide();

                                /*
                                if(postForm.modPag == "transferencia")
                                {
                                    $('div#payPalForm').hide();
                                    $('div#payTrf').show();
                                }
                                
                                if(postForm.modPag == "paypal")
                                {
                                    $('div#payPalForm').show();
                                    $('div#payTrf').hide();
                                    $('select#os0').val(postForm.modalidade);
                                    $('select#os0 option:not(:selected)').attr('disabled', true);
                                    $('select#os0 option.payTest').attr('disabled', false);
                                }
                                */

                            }
                            else if (data.msg == "mailSent") 
                            {
                                var showMsg  = "Inscrição registada com sucesso, com o número [<strong>"+data.recId+"</strong>].<br />";
                                    showMsg += "Por favor registe este número e mencione-o nos seu contactos com o Secretaria do do Congresso.<br />";
                                    showMsg += "Irá receber um email no seu endereço de registo com a cópia da informação inserida.<br />";
                                    showMsg += "Caso não o receba, por favor verifique a sua pasta de SPAM.<br />";
                                    showMsg += "Em caso de dúvida o Secretariado estará à sua disposição através do endereço de email inscricoes@alubrat.pt.<br />";
                                    showMsg += "Gratos.<br />";

                                $('#registration-msg .alert').html(showMsg);
                                $('#registration-msg .alert').removeClass("alert-danger");
                                $('#registration-msg .alert').addClass("alert-success");
                                $('#registration-msg').show();
                                $('div.payInfo').show();

                                $('#registration-submit-btn').hide();
                                $('span#continueToPay').hide();
                                $('#change-btn').hide();

                                $('select').prop('disabled', true);
                                $('input').prop('disabled', true);
                                $('select#os0').prop('disabled', false);
                                $('.pay').prop('disabled', false);

                                $("button#invoice_other_data").hide();
                                $("span#invoiceOther_Msg").hide();
                                $(".hideAtEnd").hide();

                                if(postForm.modPag == "transferencia")
                                {
                                    $('div#payPalForm').hide();
                                    $('div#payTrf').show();
                                }
                                
                                if(postForm.modPag == "paypal")
                                {
                                    $('div#payPalForm').show();
                                    $('div#payTrf').hide();
                                    $('select#os0').val(postForm.modalidade);
                                    $('select#os0 option:not(:selected)').attr('disabled', true);
                                    $('select#os0 option.payTest').attr('disabled', false);
                                }

                            }
                            else if (data.msg == "RecordExist") 
                            {
                                var warnMsg = "Endereço de email introduzido já está associado à inscrição número ["+data.recId+"]. <br />";
                                    warnMsg += "Por favor altere. <br />";
                                    warnMsg += "Se considera tratar-se de um engano, por favor contacte o Secretariado do Congresso através do endereço de email inscricoes@alubrat.pt ,<br/ > ";
                                    warnMsg += "referindo o numero de inscrição acima. <br/ > Gratos. <br />";
                                
                                $('#registration-msg .alert').html(warnMsg);
                                $('#registration-msg .alert').addClass("alert-danger");
                                $('#registration-msg').show();

                                $('select').prop('disabled', true);
                                $('input').prop('disabled', true);

                                $('#registration-submit-btn').hide();
                                $('#change-btn').show();


                            }

                            else
                            {
                                $('#registration-msg .alert').html("Registration Failed");
                                $('#registration-msg .alert').removeClass("alert-success");
                                $('#registration-msg .alert').addClass("alert-danger");
                                $('#registration-msg').show();
                            }
                        }
        });
});

function confirmInscr()
{
        $('#registration-submit-btn').hide();
        $('span#continueToPay').hide();
        $('#registration-form #confirmData').val(1);
        $('#registration-form').submit();

}

function reviewInfo()
{
    $('#registration-msg .alert').html("Rever Informação");
    $('#registration-msg .alert').removeClass("alert-danger");
    $('#registration-msg .alert').addClass("alert-success");;
    $('#registration-submit-btn').show(); 
    $('span#continueToPay').hide();
    $('#change-btn').hide();
    $('div#payPalForm').hide();
    $('div#payTrf').hide();

    $('select').prop('disabled', false);
    $('input').prop('disabled', false);

    $("button#invoice_other_data").show();
    $("span#invoiceOther_Msg").show();


}

function payPayPal()
{
    $('div#payPalForm').show();
    $('div#payTrf').hide();
}

function payTrf()
{
    $('div#payPalForm').hide();
    $('div#payTrf').show();
}

$("button#invoice_other_data").click(function()
{
    if(!$('div#invoice_other_data_fields').is(':visible'))
    {
        $('div#invoice_other_data_fields').show();
        $('input#invoiceOther').val(1);
        $("button#invoice_other_data").html("Facturar em nome do Participante");     
        $("span#invoiceOther_Msg").html(" << Clique para facturar ao próprio.");  
        $("input.form2").prop('required',true);
        $("input#f2cell").prop('required',false);
        $("input#f2phone").prop('required',false);
    }
    else
    {
        $('div#invoice_other_data_fields').hide();
        $('input#invoiceOther').val(0);
        $("button#invoice_other_data").html("Facturar em nome de outra entidade");       
        $("span#invoiceOther_Msg").html(" << Clique para inserir os dados de outra entidade a quem emitir a factura.");
        $("input.form2").prop('required',false);
    }
});
/*
 * SmoothScroll
*/

smoothScroll.init();
