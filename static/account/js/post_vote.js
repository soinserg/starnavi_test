$(function(){

  $('.btn-vote').on('click', function() {

    $.ajax({
      url: $(this).data('url'),
      method: 'POST',
      headers: {'X-CSRFToken': $.cookie('csrftoken')}
    })
      .done(function (data) {
        $('.like-count').text(data['post_info']['like_count']);
        $('.dislike-count').text(data['post_info']['dislike_count']);
      })
      .fail(function (qXHR) {
        alert(qXHR['responseText']);
      });

  });

});