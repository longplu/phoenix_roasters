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
