odoo.define('estate.backend_functionalities', function (require) {
  'use strict'

  // var formController
  var FormController = require('web.FormController')
  var ExtendFormController = FormController.include({
    saveRecord: function () {
      var res = this._super.apply(this, arguments)
      if (this.modelName == 'estate.property') {
        this.do_notify('Success', 'Record Saved!!')
      }
      return res
    },
  })
})

// FrontEnd Functionalities

odoo.define('estate.frontend_functionalities', function (require) {
  console.log("Hello there!! Hoooooray!! I'M WRITINNG JAVASCRIPT IN ODOO")

  var nextButton = document.querySelector('.next')
  var prevButton = document.querySelector('.prev')
  var slides = document.querySelectorAll('.child')

  let counter = 0

  slides.forEach(function (slide, index) {
    console.log(`${slide} Hello slides... are you there ?`)
    slide.style.left = `${index * 100}%`
  })

  //   NEXT BUTTON
  nextButton.addEventListener('click', function () {
    console.log(
      "LIFE IS GREAT I'M BEING CLICKED HERE AGAIN AND AGAIN MAN !!!! ",
    )
    counter++
    console.log(`${counter} You clicked the next button`)
    carousel()
  })

  //   PREVIOUS BUTTON

  prevButton.addEventListener('click', function () {
    counter--
    console.log(`${counter} You clicked the next button`)
    carousel()
  })

  function carousel() {
    if (counter === slides.length) {
      counter = 0
    }
    if (counter < 0) {
      counter = slides.length - 1
    }

    slides.forEach(function (slide, index) {
      slide.style.transform = `translateX(-${counter * 100}%)`
    })
  }
})
