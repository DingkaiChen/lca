$.fn.delcase=function(){
	var row=$(this).parent().parent();
	var id=row.find('#caseid').text();
	var name=row.find('#name').text();
	$('#delModal').find('#del-id').text(id);
	$('#delModal').find('#del-name').text(name);
	$('#delModal').find('#del-message').text('确认删除案例 <'+name+'> 吗？');
}

$(document).ready(function(){
	$('#cases').find('.del').click(function(){
		$(this).delcase();
	});
	
	$('#del-confirm').click(function(){
		$('.alert-info').attr('style','display:none;');
		var caseid=$('#delModal').find('#del-id').text();
		var casename=$('#delModal').find('#del-name').text();
		$.post('delcase',{
			id:caseid,
		},
		function(result){
			if(result=='fail')
			{
				$('#alert').text("删除失败！");	
				$('#alert').attr('class','alert alert-warning')
				$('#alert').attr('style','');
			}
			else
			{
				$('#cases').text("");
				$('#cases').append(result);
				$('#alert').text("案例 <"+casename+"> 已成功删除.");
				$('#alert').attr('class','alert alert-success');
				$('#alert').attr('style','');
				$('#cases').find('.del').click(function(){
					$(this).delcase();
				});
			}
		});
	});
});
	
