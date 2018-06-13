$(document).ready(function () {
    var layer=layui.layer
    $('#Login').on('click',function () {
        var username=$("#username").val()
        var password=$('#userpass').val()
        var body={
            username:username,
            password:password,
        }
        $.ajax({
            url:'/ajax/',
            type:'POST',
            data:{
                action:'Login',
                body:body,
                type:'query',
            },
            success:function(callback){
                var callback_dict = $.parseJSON(callback);
                if (callback_dict.status==true){
                    layer.msg(callback_dict.msg);
                }else{
                    // $('#status').text(callback_dict.error);
                    // $('#status').removeClass('success').addClass('error')
                    layer.msg(callback_dict.msg);
                }
            }
        })
    });
})