$(document).ready(function() {
	$('.salonsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  infinite: true,
	  prevArrow: $('.salons .leftArrow'),
	  nextArrow: $('.salons .rightArrow'),
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});
	$('.servicesSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.services .leftArrow'),
	  nextArrow: $('.services .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.mastersSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.masters .leftArrow'),
	  nextArrow: $('.masters .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.reviewsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.reviews .leftArrow'),
	  nextArrow: $('.reviews .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	// menu
	$('.header__mobMenu').click(function() {
		$('#mobMenu').show()
	})
	$('.mobMenuClose').click(function() {
		$('#mobMenu').hide()
	})


	var acc = document.getElementsByClassName("accordion");
	var i;

	for (i = 0; i < acc.length; i++) {
	  acc[i].addEventListener("click", function(e) {
	  	e.preventDefault()
	    this.classList.toggle("active");
	    var panel = $(this).next()
	    panel.hasClass('active') ?  
	    	 panel.removeClass('active')
	    	: 
	    	 panel.addClass('active')
	  });
	}


	$(document).on('click', '.accordion__block', function(e) {
		let thisName,thisAddress;

		thisName = $(this).find('> .accordion__block_intro').text()
		thisAddress = $(this).find('> .accordion__block_address').text()
		
		
		if(thisName === 'BeautyCity Пушкинская') {
			$('.service__masters > .panel').html(`
				<div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/all.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Любой мастер</div>
						  	</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/1.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Елизавета Лапина</div>
						  	</div>
						  	<div class="accordion__block_prof">Мастер маникюра</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/2.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Анна Сергеева</div>
						  	</div>
						  	<div class="accordion__block_prof">Парикмахер</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/3.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Ева Колесова</div>
						  	</div>
						  	<div class="accordion__block_prof">Визажист</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/4.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Мария Суворова</div>
						  	</div>
						  	<div class="accordion__block_prof">Стилист</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/5.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Мария Максимова</div>
						  	</div>
						  	<div class="accordion__block_prof">Визажист</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/6.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Анастасия Сергеева</div>
						  	</div>
						  	<div class="accordion__block_prof">Визажист</div>
						  </div>	
			`)
			// $('.service__masters div[data-masters="Pushkinskaya"]').addClass('vib')
		}
		console.log(thisName)
		if(thisName === 'BeautyCity Ленина') {
			
			$('.service__masters > .panel').html(`
				<div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/all.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Любой мастер</div>
						  	</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/1.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Дарья Мартынова</div>
						  	</div>
						  	<div class="accordion__block_prof">Мастер маникюра</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/2.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Амина Абрамова</div>
						  	</div>
						  	<div class="accordion__block_prof">Парикмахер</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/3.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Милана Романова</div>
						  	</div>
						  	<div class="accordion__block_prof">Визажист</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/4.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Диана Чернова</div>
						  	</div>
						  	<div class="accordion__block_prof">Стилист</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/5.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Полина Лукьянова</div>
						  	</div>
						  	<div class="accordion__block_prof">Визажист</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/6.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Вера Дмитриева</div>
						  	</div>
						  	<div class="accordion__block_prof">Визажист</div>
						  </div>
			`)
		}

		if(thisName === 'BeautyCity Красная') {
			$('.service__masters > .panel').html(`
				<div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/all.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Любой мастер</div>
						  	</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/1.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Зоя Матвеева</div>
						  	</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/2.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Мария Родина</div>
						  	</div>
						  	<div class="accordion__block_prof">Мастер маникюра</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/3.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Дарья Попова</div>
						  	</div>
						  	<div class="accordion__block_prof">Парикмахер</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/4.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Ева Семенова</div>
						  	</div>
						  	<div class="accordion__block_prof">Визажист</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/5.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Вера Романова</div>
						  	</div>
						  	<div class="accordion__block_prof">Стилист</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/6.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">Валерия Зуева</div>
						  	</div>
						  	<div class="accordion__block_prof">Визажист</div>
						  </div>
			`)
			
		}

		$(this).parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		setTimeout(() => {
			$(this).parent().parent().find('> button.active').click()
		}, 200)
		
		// $(this).parent().addClass('hide')

		// console.log($(this).parent().parent().find('.panel').hasClass('selected'))
		
		// $(this).parent().parent().find('.panel').addClass('selected')
	})


	$('.accordion__block_item').click(function(e) {
		let thisName,thisAddress;
		thisName = $(this).find('> .accordion__block_item_intro').text()
		thisAddress = $(this).find('> .accordion__block_item_address').text()
		thisId = $(this).find('> .accordion__block_item_id').text()
		console.log(thisId)
		$(this).parent().parent().parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		$(this).parent().parent().parent().parent().find('> button.active').attr('id', thisId)
		// $(this).parent().parent().parent().parent().find('> button.active').click()
		// $(this).parent().parent().parent().addClass('hide')
		setTimeout(() => {
			$(this).parent().parent().parent().parent().find('> button.active').click()
		}, 200)
	})



	// 	console.log($('.service__masters > .panel').attr('data-masters'))
	// if($('.service__salons .accordion.selected').text() === "BeautyCity Пушкинская  ул. Пушкинская, д. 78А") {
	// }


	$(document).on('click', '.service__masters .accordion__block', function(e) {
		let clone = $(this).clone()
		clone.addClass('selected-master')
		thisId = console.log(clone.find('> .masterId').text())
		$(this).parent().parent().find('> button.active').html(clone).attr('id', thisId)
		
		date = $('#datepickerHere').val()
		console.log(date)
			var selectedDate = date;
			var timeSlotsContainer = $('.time__elems_elem');
			timeSlotsContainer.empty();
			if(!$('.time__items .time__elems_elem .time__elems_btn').hasClass('active')) {
				$('.time__btns_next').attr('disabled', '');
				$('.time__btns_next').removeClass('active');
			};
			$.ajax({
				url: '/booking/get-time/',
				data: {
					date: selectedDate,
					employeeId: $('.selected-master #masterId').text()
				},
				success: function(response) {
					var morningContainer = $('.time__elems_intro:contains("Утро")').next('.time__elems_elem');
					var dayContainer = $('.time__elems_intro:contains("День")').next('.time__elems_elem');
					var eveningContainer = $('.time__elems_intro:contains("Вечер")').next('.time__elems_elem');

					morningContainer.empty();
					dayContainer.empty();
					eveningContainer.empty();
					
					for (var i = 0; i < response.available_time_slots.length; i++) {
						var timeSlot = response.available_time_slots[i];
						var timeSlotButton = '<button data-time="' + timeSlot + '" class="time__elems_btn">' + timeSlot + '</button>';
						
						if (timeSlot >= '06:00' && timeSlot < '12:00') {
						  morningContainer.append(timeSlotButton);
						} else if (timeSlot >= '12:00' && timeSlot < '17:00') {
						  dayContainer.append(timeSlotButton);
						} else {
						  eveningContainer.append(timeSlotButton);
						}
					}
				}
			});
	})

	// $('.accordion__block_item').click(function(e) {
	// 	const thisName = $(this).find('.accordion__block_item_intro').text()
	// 	const thisAddress = $(this).find('.accordion__block_item_address').text()
	// 	console.log($(this).parent().parent().parent().parent())
	// 	$(this).parent().parent().parent().parent().find('button.active').addClass('selected').text(thisName + '  ' +thisAddress)
	// })



	// $('.accordion__block_item').click(function(e) {
	// 	const thisChildName = $(this).text()
	// 	console.log(thisChildName)
	// 	console.log($(this).parent().parent().parent())
	// 	$(this).parent().parent().parent().parent().parent().find('button.active').addClass('selected').text(thisChildName)

	// })
	// $('.accordion.selected').click(function() {
	// 	$(this).parent().find('.panel').hasClass('selected') ? 
	// 	 $(this).parent().find('.panel').removeClass('selected')
	// 		:
	// 	$(this).parent().find('.panel').addClass('selected')
	// })


	//popup
	$('.header__block_auth').click(function(e) {
		e.preventDefault()
		$('#authModal').arcticmodal();
		// $('#confirmModal').arcticmodal();

	})

	$(document).ready(function() {
        $('.policy-link').click(function(e) {
            e.preventDefault();
            $('#footer__linkModal').arcticmodal();
        });
    });

	$('.footer__link').click(function(e) {
        e.preventDefault();
        $('#footer__linkModal').arcticmodal();
    });

	$('#callback_button').on('click', function() {
        $('#call_me_back').arcticmodal();
    });

	$('.rewiewPopupOpen').click(function(e) {
		e.preventDefault()
		$('#reviewModal').arcticmodal();
	})
	$('.payPopupOpen').click(function(e) {
		e.preventDefault()
		$('#paymentModal').arcticmodal();
	})
	$('.tipsPopupOpen').click(function(e) {
		e.preventDefault()
		$('#tipsModal').arcticmodal();
	})
	
	$('.authPopup__form:not(#call_me_back form)').submit(function() {
        $('#confirmModal').arcticmodal();
        return false
	})
	$(document).ready(function(){
        $('#call_me_back form').on('submit', function(e) {
            e.preventDefault();
            $.arcticmodal('close');
            $('#thanksModal').arcticmodal();
        });
    });

    $(document).ready(function(){
        $('.authPopup__form').on('submit', function(e) {
            var phoneNumber = $(this).find('input[name="tel"]').val();
            var phoneRegExp = /^\+7\d{10}$/;

            if (!phoneRegExp.test(phoneNumber)) {
                e.preventDefault();
                alert('Введите номер телефона в формате +79999999999');
            } else {
                if ($(this).parent().attr('id') === 'call_me_back') {
                    e.preventDefault();
                    $.arcticmodal('close');
                    $('#thanksModal').arcticmodal();
                } else {
                    e.preventDefault();
                    $('#confirmModal').arcticmodal();
                }
            }
        });
    });

    $('.review__link').click(function(e) {
      e.preventDefault();
      window.location.href = $(this).attr('href');
    });

	// datepicker
	new AirDatepicker('#datepickerHere', {
		toggleSelected: false,
		minDate: new Date(),
		onSelect(date){
			console.log(date.formattedDate)
			var selectedDate = date.formattedDate;
			var timeSlotsContainer = $('.time__elems_elem');
			timeSlotsContainer.empty();
			if(!$('.time__items .time__elems_elem .time__elems_btn').hasClass('active')) {
				$('.time__btns_next').attr('disabled', '');
				$('.time__btns_next').removeClass('active');
			};
			$.ajax({
				url: '/booking/get-time/',
				data: {
					date: selectedDate,
					employeeId: $('.selected-master #masterId').text()
				},
				success: function(response) {
					var morningContainer = $('.time__elems_intro:contains("Утро")').next('.time__elems_elem');
					var dayContainer = $('.time__elems_intro:contains("День")').next('.time__elems_elem');
					var eveningContainer = $('.time__elems_intro:contains("Вечер")').next('.time__elems_elem');

					morningContainer.empty();
					dayContainer.empty();
					eveningContainer.empty();
					
					for (var i = 0; i < response.available_time_slots.length; i++) {
						var timeSlot = response.available_time_slots[i];
						var timeSlotButton = '<button data-time="' + timeSlot + '" class="time__elems_btn">' + timeSlot + '</button>';
						
						if (timeSlot >= '06:00' && timeSlot < '12:00') {
						  morningContainer.append(timeSlotButton);
						} else if (timeSlot >= '12:00' && timeSlot < '17:00') {
						  dayContainer.append(timeSlotButton);
						} else {
						  eveningContainer.append(timeSlotButton);
						}
					}
				}
			});
		}
	});

	//service
	$('.time__items .time__elems_elem').on('click', '.time__elems_btn', function(e) {
		e.preventDefault()
		$('.time__elems_btn').removeClass('active')
		$(this).addClass('active')
		$('.time__btns_next').removeAttr('disabled')
		$('.time__btns_next').addClass('active')
		// $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
	})

	$(document).on('click', '.main', function() {
		if(!$('.time__items .time__elems_elem .time__elems_btn').hasClass('active')) {
			$('.time__btns_next').attr('disabled', '')
			$('.time__btns_next').removeClass('active')
		}
	})

	function setFormValues(selectedService, selectedEmployee, selectedDate, selectedTime) {
		$('#service-input').val(selectedService);
		$('#employee-input').val(selectedEmployee);
		$('#date-input').val(selectedDate);
		$('#time-input').val(selectedTime);
	}

	$('.time__btns_next').on('click', function(e) {
		e.preventDefault()

		var selectedService = $('.service__services button.selected').attr('id');
		var selectedEmployee = $('.selected-master .masterId').text();
		var selectedDate = $('#datepickerHere').val();
		var selectedTime = $('.time__elems_btn.active').data('time');
	  
		setFormValues(selectedService, selectedEmployee, selectedDate, selectedTime);
	  
		$('.service__form').closest('form').submit();
	  });
})
