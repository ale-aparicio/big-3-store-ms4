/* Set product rating stars for all divs with the class product-rating-stars */
$('.product-rating-stars').each(function () {
    let productRating = $(this).data("product-rating");
    if ((productRating == "None") || (productRating == null) || (productRating == ""))
        $(this).html("<i class=rating-text>Not Rated</i>");
    else {
        let productRatingRounded = (Math.round(productRating));
        let stars = $(this).children();
        stars.each(function(si) {
            if (productRatingRounded > si) {
                $(this).addClass("fg-yellow");
            }
        });
    }
});


/* On click event handlers added to product review edit stars */
/* Note, updates the hidden form input rating with the selected rating */
$('.product-review-edit-stars').each(function () {
    let currentRating = $(this).data("product-rating");
    let stars = $(this).children();
    stars.each(function(si) {
        if (currentRating > si) {
            $(this).addClass("fg-yellow");
        }
        $(this).click(function() {
            let starId = $(this).attr('id');
            let rating = parseInt(starId.slice(-1));
            colourStars(rating, "#star-");
        });
    });
});


// On click event handler added to review delete buttons to build delete confirmation modal dialog
$('.reviewDeleteBtn').each(function () {
    let btnId = "#" + $(this).attr("id");
    $(btnId).click(function() {
        (buildConfirmModal(btnId, "#confirmModal"));
    });
});


/**
* [Function to add yellow colour class to stars]
* @return {[rating]}                     [rating, integer]          
*/
function colourStars(rating, starIdPrefix) {

    // Remove yellow class from all rating stars
    for (let i = 1; i <= 5; i++) {
        $(starIdPrefix + i).removeClass("fg-yellow");
    }
    // Add yellow class to correct rating stars
    for (let i = 1; i <= rating; i++) {
        $(starIdPrefix + i).addClass("fg-yellow");
    }
    $('input[name=rating]').val(rating);
    return rating;
}