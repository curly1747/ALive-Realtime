"use strict";

var KTPage = function () {
    var default_img = document.createElement('img');
    default_img.src = "static/screenshot/default.png"
    default_img.classList = "stream-thumbnail radius-10";

    var img = document.createElement('img');
    img.classList = "stream-thumbnail radius-10";

    let image_load_handle = () => {
        $(".stream-thumbnail").each((i, obj) => {
            let img = document.createElement('img');
            img.src = $(obj).attr("data-src");
            img.onload = () => {
                img.classList = "stream-thumbnail radius-10";
                $(obj).replaceWith(img);
            }
        })
    }

    let refresh_init = () => {
        $.ajax({
            type: 'GET',
            url: '/current_stream',
            dataType: 'json',
            success: function (data) {
                let stream_thumbnail = $(".col-xl-2")
                $.each(data, (i, stream) => {
                        let image = img;
                        image.src = "static/screenshot/" + stream['userId'] + ".jpg?" + new Date().getTime();
                        image.onerror = () => {
                            console.log('error ' + stream['userId']);
                            image = default_img;
                        }
                        let ele = null;
                        ele = HTMLRender.streamThumbnail(
                            stream['userId'], stream['displayName'], stream['title'] ,stream['score'], stream['verified'], image.outerHTML, stream['packages']
                        );
                        (i < stream_thumbnail.length) ? $(stream_thumbnail[i]).replaceWith(ele) : $(".row").append(ele)
                    }
                )
                if (data.length < stream_thumbnail.length) {
                    for (let i = data.length; i < stream_thumbnail.length; i++) {
                        stream_thumbnail[i].remove();
                    }
                }
            },
            error: function (xhr) {
            }
        })
    }

    let quick_action_handle = () => {
        $( ".ban-stream" ).on('click', async (e) => {
            const ban_reason = {
                'sex': 'Nội dung đồi trụy',
                'idle': 'Treo cam',
                'harassment': 'Quấy rối idol'
            }
            const { value: reason } = await Swal.fire({
                title: 'Please select ban reason',
                input: 'select',
                inputOptions: ban_reason,
                inputPlaceholder: 'Ban reason',
                showCancelButton: true,
                inputValidator: (value) => {
                    return new Promise((resolve) => {
                        if (value) {
                            resolve()
                        } else {
                            resolve('You need to select reason')
                        }
                    })
                }
            })

            if (reason) {
                $.ajax({
                    type: 'GET',
                    url: '/ban',
                    data: {'user_id': $(e.currentTarget).attr('data-user-id'), 'reason': ban_reason[reason]},
                    dataType: 'json',
                    success: function (data) {
                        Swal.fire($(e.currentTarget).attr('data-user-id') + ' has been banned');
                    },
                    error: function (xhr) {
                        console.log(xhr);
                    }
                })
            }
        })

        $( ".delete-stream" ).on('click', async (e) => {
            const delete_reason = {
                'idle': 'Treo cam'
            }
            const { value: reason } = await Swal.fire({
                title: 'Please select reason',
                input: 'select',
                inputOptions: delete_reason,
                inputPlaceholder: 'Ban reason',
                showCancelButton: true,
                inputValidator: (value) => {
                    return new Promise((resolve) => {
                        if (value) {
                            resolve()
                        } else {
                            resolve('You need to select reason')
                        }
                    })
                }
            })

            if (reason) {
                $.ajax({
                    type: 'GET',
                    url: '/delete_stream',
                    data: {'room_id': $(e.currentTarget).attr('data-user-id')},
                    dataType: 'json',
                    success: function (data) {
                        Swal.fire($(e.currentTarget).attr('data-user-id') + ' has been deleted');
                    },
                    error: function (xhr) {
                        console.log(xhr);
                    }
                })
            }
        })
    }

    // Public methods
    return {
        init: async function () {
            image_load_handle();
            quick_action_handle();
            setInterval(
                () => {
                    refresh_init()
                }, 60*1000
            )
        }
    }
}();

// On document ready
KTUtil.onDOMContentLoaded( async function () {
    await KTPage.init();
    pageReady();
});