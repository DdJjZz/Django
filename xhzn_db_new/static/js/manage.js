$(document).ready(function () {
    close_windews();
    get_menulist();
    $('#Menu_Manage').css('display','block');
    $('#menu').on('click',function () {
        close_windews();
        $('#Menu_Manage').css('display','block');
    });
    $('#action').on('click',function () {
        close_windews();
        $('#Action_Manage').css('display','block');
    });
    $('#user').on('click',function () {
        close_windews();
        $('#User_Manage').css('display','block');
    });
    $('#user_group').on('click',function () {
        close_windews();
        $('#UserGroup').css('display','block');
    });
    $('#project_group').on('click',function () {
        close_windews();
        $('#ProjectGroup').css('display','block');
    });
    $('#project').on('click',function () {
        close_windews();
        $('#Project_Manage').css('display','block');
    });
    $('#site').on('click',function () {
        close_windews();
        $('#Site_Manage').css('display','block');
    });
});
function close_windews(){
    $('.Menu_windows').css('display','none');
}
function ajax_function(url,data,type){
    $.ajax({
        url:url,
        type:type,
        data:data,
        success:function (data) {
            data=JSON.parse(data)
        }
    });
}
function get_menulist(){
    $.ajax({
        url:"/ajax/",
        type:'POST',
        data:{
            action:'MenuList',
            type:'query',
        },
        success:function (data) {
            data=JSON.parse(data)
            var codelist=data.status.code;
            var namelist=data.status.name;
            if(data.ret==true){
                bulidmenulist(codelist,namelist);
            }
        }
    });
}

function bulidmenulist(code,name) {
    // var menulist="<option value='all' selected=''>全部菜单</option>"
    var codelist="";
    var namelist="";
    for(var i=0;i<code.length;i++){
        codelist=codelist+"<option value="+code[i]+">"+code[i]+"</option>";
        namelist=namelist+"<option value="+code[i]+">"+name[i]+"</option>";
    }
    $("#Code_select").empty();
    $("#Code_select").append(codelist);
    $("#Name_select").empty();
    $("#Name_select").append(namelist);
}