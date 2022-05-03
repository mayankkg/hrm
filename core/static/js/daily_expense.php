<?php 
	$this->load->view('partials/header');
	$this->load->view("partials/sidebar");
	$login_sess=$this->session->userdata("admin");
	
?>

<style>
/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}
</style>
<!-- date picker-->
<link rel="stylesheet" href="<?php echo asset_url()?>libs/flatpickr/flatpickr.min.css">
<div class="main-content" id="miniaresult">
 <div class="page-content">
    <div class="container-fluid">
		<?php 
		if($this->session->flashdata('success_msg')){
			echo '<div class="alert alert-success alert-dismissible fade show" role="alert">'
					.$this->session->flashdata('success_msg').'
					<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
				</div>';
		}
		if($this->session->flashdata('error_msg')){
			echo '<div class="alert alert-danger alert-dismissible fade show" role="alert">'
					.$this->session->flashdata('error_msg').'
					<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
				</div>';
		}
		if(validation_errors()){
			echo '<div class="alert alert-danger alert-dismissible fade show" role="alert">'
					.validation_errors().'
					<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
				</div>';
		}
		
		?>
        <!-- start page title -->
        <div class="row">
            <div class="col-12">
                <div class="page-title-box d-sm-flex align-items-center
                    justify-content-between">
                    <h4 class="mb-sm-0 font-size-18">Daily Expense Manager</h4>

                    <div class="page-title-right">
                        <ol class="breadcrumb m-0">
                            <li class="breadcrumb-item"><a href="javascript:
                                    void(0);">HRM</a></li>
                            <li class="breadcrumb-item active">Daily Expense Manager</li>
                        </ol>
                    </div>

                </div>
            </div>
        </div>
        <!-- end page title -->

        <div class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header">
                        <!--<h4 class="card-title">Textual inputs</h4>
                        <p class="card-title-desc">Enter basic details of <code>Prospect</code></p>-->
                    </div>
                    <div class="card-body p-4">
					<?php
					if($_GET['exp_id']){
						$action_url=site_url('daily_expense?exp_id='.$_GET['exp_id']);
					}else{
						$action_url=site_url('daily_expense');
					}
					?> 
					<form class="custom-form needs-validation" novalidate action="<?php echo $action_url; ?>" method="post"  enctype="multipart/form-data">
						<input type="hidden" name="form_exp_id" value="<?php echo $get_edit['de_id']?>">						
						<input type="hidden" name="old_bill_pic" value="<?php echo $get_edit['bill_pic']?>"> 
                        <div class="row">
                            <div class="col-lg-12">
                                <div>
									<div class="row">
										<div class="col-md-6">
											<div class="mb-3">
												<label for="current_date" class="form-label">Current Date (MM-DD-YY)</label>
												<input class="form-control" type="text" name="current_date" value="<?php echo date('m-d-Y')?>" id="current_date" title="Current Date" readonly>
											</div>
										</div>
										<div class="col-md-6">
											<div class="mb-3">
												<label for="transaction_date" class="form-label">Transaction Date* (MM-DD-YY)</label>
												<?php 
												if($get_edit['de_id']){
													$pre_fixed_date=date('m-d-Y',strtotime($get_edit['expense_date']));
												}else{
													$pre_fixed_date=date('m-d-Y');
												}
												?>
												<input class="form-control" type="text" value="<?php if($get_edit['expense_date']!=""){ echo date('m-d-Y',strtotime($get_edit['expense_date'])); } ?>" name="date" id="datepicker-basic" title="Transaction Date" required>
											</div>
										</div>
									</div>
									<div class="row">
										<div class="col-md-6">
											<div class="mb-3">
												<label class="form-label">Expense Type*</label>
												<select class="form-select Exp_Type" name="type" title="Expense Type" id="type" required>
													<?php
													echo "<option value=''>Select Expense Type</option>"; 
													if(!empty($types)){
														foreach($types as $typek=>$typev){
															if($typev['id']==show_value('type',$get_edit['type'])){
																echo "<option selected value='".$typev['id']."'>".$typev['name']."</option/>";
															}else{
																echo "<option value='".$typev['id']."'>".$typev['name']."</option/>";
															}								
														}
													}
													?>
												</select>
											</div>
										</div>
										<div class="col-md-6">
											<div class="mb-3">
												<label class="form-label">Expense Head Group</label>
												<select class="form-select" name="type" title="Expense Type" id="type" required>
													<?php
													echo "<option value=''>Select Expense Type</option>"; 
													if(!empty($types)){
														foreach($types as $typek=>$typev){
															if($typev['id']==show_value('type',$get_edit['type'])){
																echo "<option selected value='".$typev['id']."'>".$typev['name']."</option/>";
															}else{
																echo "<option value='".$typev['id']."'>".$typev['name']."</option/>";
															}								
														}
													}
													?>
												</select>
											</div>
										</div>
									</div>
									<div class="row">
										<div class="col-md-6">
											<div class="mb-3">
												<label for="currency_formater" class="form-label">Amount*</label>
												<input class="form-control" type="text" name="amount" value="<?php echo show_value('amount',$get_edit['amount'])?>" id="currency_formater" title="Amount" placeholder="Enter Amount" required>
											</div>
										</div>
										<div class="col-md-6">
											<div class="mb-3">
												<label class="form-label">Payment Mode*</label>
												<select class="form-select" name="mode" id="mode" title="Mode" required>
													<?php 
													echo "<option value=''>Select Mode</option>";
													if(!empty($modes)){
														foreach($modes as $modesk=>$modesv){
															if($modesv['id']==show_value('mode',$get_edit['mode'])){
																echo "<option selected value='".$modesv['id']."'>".$modesv['mode']."</option/>";
															}else{
																echo "<option value='".$modesv['id']."'>".$modesv['mode']."</option/>";
															}
														}
													}
													?>
												</select>
											</div>
										</div>
									</div>
									<div class="row">
										
										<div class="col-md-6">
											<div class="mb-3">
												<label for="comment" class="form-label">Comment*</label>
												<input class="form-control"  placeholder="Enter Comment" value="<?php echo show_value('comment',$get_edit['comment'])?>" type="text" id="comment" name="comment" title="Comment" placeholder="Enter Amount" required>
											</div>
										</div>
										<div class="col-md-6">
											<div class="mb-3">
												<label for="ctc_offered" class="form-label">Receipt Pic*</label>
												<input class="form-control" type="file" name="file" onchange="readURL(this);" title="Receipt Pic" >
												<?php
												if($get_edit['bill_pic']){
													$bill_pic_url=asset_url()."bills/".$get_edit['bill_pic'];
													$display_style="";
												}else{
													$display_style="style='display:none;'";
													$bill_pic_url="#";
												}
												?>
												<a <?php echo $display_style;?> target="_blank" href="<?php echo $bill_pic_url;?>"><img style="width:150px;height:200px;" id="blah" src="<?php echo $bill_pic_url;?>"/></a>
											</div>
										</div>
									</div>
									<!--<div class="row">
										<div class="col-md-6">
											<div class="mb-3">
												<label class="form-label">Client</label>
												<select class="form-select" name="client" id="client" title="Client">
													<?php
													echo "<option value=''>Select Client</option>"; 
													if(!empty($clients)){
														foreach($clients as $ck=>$client_v){
															if($client_v['id']==show_value('client',$get_edit['client_id'])){
																echo "<option selected value='".$client_v['id']."'>".$client_v['name']."</option/>";
															}else{
																echo "<option value='".$client_v['id']."'>".$client_v['name']."</option/>";
															}								
														}
													}
													?>
												</select>
											</div>
										</div>
										<div class="col-md-6">
											<div class="mb-3">
												<label class="form-label">Project</label>
												<select class="form-select" name="project" id="project" title="Project">
													<?php
													echo "<option value=''>Select Project</option>"; 
													if(!empty($projects)){
														foreach($projects as $pk=>$proj_v){
															if($proj_v['id']==show_value('project',$get_edit['project'])){
																echo "<option selected value='".$proj_v['id']."'>".$proj_v['project_name']."</option/>";
															}else{
																echo "<option value='".$proj_v['id']."'>".$proj_v['project_name']."</option/>";
															}								
														}
													}
													?>
												</select>
											</div>
										</div>
									</div>-->
									<div class="row">
										
									</div>
									
									<div class="row">
										<div class="col-md-6">
											<div class="mt-4">
                                                <button type="submit" class="btn btn-primary w-md">Submit</button>
                                            </div>
										</div>
									</div>
                                </div>
                            </div>
							</div>
							</form>
						</div>
					</div>
				</div> <!-- end col -->
			</div>
			<!-- end row -->

		</div> <!-- container-fluid -->
	</div>
</div>
                    <!-- End Page-content -->
<?php $this->load->view('partials/footer');?>

<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<!-- datepicker js -->
<script src="<?php echo asset_url()?>libs/flatpickr/flatpickr.min.js"></script>
<script>
flatpickr('#datepicker-basic', {
  dateFormat: "m-d-Y",
   onClose: function (selectedDate) {                                           
	//console.log(selectedDate['0']);
	var year = selectedDate['0'].getFullYear();
	var month = selectedDate['0'].getMonth() + 1;
	var day = selectedDate['0'].getDate();
	

   }
});
</script>
<script>
/*client manager email id autosuggest functionality*/
  $( function() {
	
    $(".job_location").autocomplete({
    	 source: function (request, response) {
    	        jQuery.get("<?php echo site_url('add_prospect/get_auto_cities')?>",{
    	            query: request.term
    	        }, function (data) {
    	            response(JSON.parse(data));
    	           // console.log(JSON.parse(data));
    	        });
    	    },
        minLength: 3,
        select: function (event, ui) {
            var label = ui.item.label;
            var tax_rate = ui.item.tax_rate;
            $("#Tax_Rate").val(tax_rate);
            $(".city_tax_rate").val(tax_rate);
            //extract_net_bill_rate();
            
        }
      }).focus(function(){            
       $(this).data("uiAutocomplete").search($(this).val());
  });

    
  } );
</script>
<script>
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()
</script>
<script src="<?php echo asset_url()?>jquery.maskMoney.min.js" type="text/javascript"></script>
<script>
  $(function() {
    $('#currency_formater').maskMoney();
  })
</script>
<script>
  function readURL(input) {
	  $("#blah").show();
      if (input.files && input.files[0]) {
          var reader = new FileReader();

          reader.onload = function (e) {
        	  $('#blah').parent().attr('href', e.target.result);
              
              $('#blah')
                  .attr('src', e.target.result)
                  .width(150)
                  .height(200);
          };

          reader.readAsDataURL(input.files[0]);
      }
  }
  </script>
  <script>
  $(".Exp_Type").change(function(){
	  var exp_type = $(this).val();
	  var exp_date = $("#datepicker-basic").val();
	  var spl_date = exp_date.split("-");
	  var month = spl_date['0'];
	  var date = spl_date['1'];
	  var year = spl_date['2'];
	  
  });
  
  function get_budget(exp_type,month,year){
	   $.post("<?php echo site_url('daily_expense/get_total_budget');?>",{"exp_type":exp_type,"month":month,"year":year},function(data){
		
		});	
	
  }
  </script>