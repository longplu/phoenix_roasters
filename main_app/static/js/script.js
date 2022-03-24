// variables
const shoppingcartsEditQuantity = document.getElementById("");
const shoppingcartsAdd = document.getElementById("#shoppingcarts-add");
const shoppingcartsForm = document.getElementById("#shoppingcarts-form");

const overlay = $("#overlay");
const searchBtn = $("#search-button");

//
searchBtn.on("click", function () {
  $(".search").removeClass("search__hide");
  overlay.addClass("overlay__show");
});

$(".home_fav__products__slick").slick({
  infinite: true,
  slideToShow: 4,
  slidesToScroll: 1,
  arrow: false,
  dots: false,
  autoplay: true,
  autoplaySpeed: 5000,
  responsive: [
    {
      breakpoint: 550,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
      },
    },
    {
      breakpoint: 990,
      setting: {
        slideToShow: 4,
        slidesToScroll: 1,
      },
    },
  ],
});
