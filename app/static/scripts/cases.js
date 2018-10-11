$.fn.delcase=function(){
	var row=$(this).parent().parent();
	var id=row.find('.caseid').text();
	var name=row.find('.name').text();
	$('#delModal').find('#del-id').text(id);
	$('#delModal').find('#del-name').text(name);
	$('#delModal').find('#del-message').text('确认删除案例 <'+name+'> 吗？');
}

$.fn.drawchart=function(){
	var cases=new Array();
	var effs=new Array();
	$('#cases').find('.name').each(function(){
		cases.push($(this).text());
	});
	$('#cases').find('.efficiency').each(function(){
		effs.push(parseFloat($(this).text()));
	});
	var options={
		chart:{
			type:'column'
		},
		title:{
			text:'化工企业生命周期能耗'
		},
		xAxis:{
			categories:cases,
			crosshair:true
		},
		yAxis:{
			min:0,
			title:{
				text:'单位尿素生命周期能耗（吨标准煤）'
			}
		},
		series:[{
			name: '效率',
			data: effs
		}]
	};
	var chart=Highcharts.chart('container',options);
}

$(document).ready(function(){
	$('#cases').find('.del').click(function(){
		$(this).delcase();
	});

	$('#container').drawchart();
	
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
	
