
const HTMLRender = {
    text: function (text, style = "muted", inline = false) {
        const style_cls = {
            muted: 'text-muted fw-bold',
            dark: 'text-dark fw-bolder',
        }
        const inline_cls = {
            true: 'd-block',
            false: '',
        }
        return `<span class="${style_cls[style]} ${inline_cls[inline]} mb-1">${text}</span>`
    },
    link: function (text, link = "#", style = "muted", inline = false) {
        const style_cls = {
            'muted': 'text-muted fw-bold',
            'dark': 'text-dark fw-bolder',
        }
        const inline_cls = {
            true: 'd-block',
            false: '',
        }
        return `<a href="${link}" class="${style_cls[style]} ${inline_cls[inline]} text-hover-primary mb-1 fs-6">${text}</a>`;
    },
    badge: function (text, style = "primary", inline = false) {
        const inline_cls = {
            true: 'd-block',
            false: '',
        }
        return `<span class="badge badge-${style}">${text}</span>`;
    },
    process_bar: function (percent, style = "primary", height_px = 5, width_percent = 75) {
        percent *= 100;
        style = style.replace('light-', '');
        return `<div class="progress h-${height_px}px w-${width_percent}">
                    <div class="progress-bar bg-${style}" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0"
                         aria-valuemax="100"></div>
                </div>`
    },
    menu: function (text, items) {
        let menu_item = function (text, link = "#") {
            return `
                <!--begin::Menu item-->
                <div class="menu-item px-3">
                    <a href="${link}" class="menu-link px-3">
                        ${text}
                    </a>
                </div>
                <!--end::Menu item-->
            `;
        }
        return `
            <a href="#" class="btn btn-light btn-active-light-primary btn-sm" data-kt-menu-trigger="click" data-kt-menu-placement="bottom-end" data-kt-menu-flip="top-end">
                ${text}
                <span class="svg-icon svg-icon-5 m-0">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">
                        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <polygon points="0 0 24 0 24 24 0 24"></polygon>
                            <path d="M6.70710678,15.7071068 C6.31658249,16.0976311 5.68341751,16.0976311 5.29289322,15.7071068 C4.90236893,15.3165825 4.90236893,14.6834175 5.29289322,14.2928932 L11.2928932,8.29289322 C11.6714722,7.91431428 12.2810586,7.90106866 12.6757246,8.26284586 L18.6757246,13.7628459 C19.0828436,14.1360383 19.1103465,14.7686056 18.7371541,15.1757246 C18.3639617,15.5828436 17.7313944,15.6103465 17.3242754,15.2371541 L12.0300757,10.3841378 L6.70710678,15.7071068 Z" fill="#000000" fill-rule="nonzero" transform="translate(12.000003, 11.999999) rotate(-180.000000) translate(-12.000003, -11.999999)"></path>
                        </g>
                    </svg>
                </span>
            </a>
            <!--begin::Menu-->
            <div class="menu menu-sub menu-sub-dropdown menu-column menu-rounded menu-gray-600 menu-state-bg-light-primary fw-bold fs-7 w-125px py-4" data-kt-menu="true">
                ${items.map(i => menu_item(i.text, i.link)).join("")}
            </div>
            <!--end::Menu-->
        `;
    },
    button: function (text, link = "") {
        return `<a href="${link}" class="btn btn-light-primary">${text}</a>`;
    },
    carousel: function (id, title, items) {
        let indicator = function (id, len, active = true, index = 0) {
            if (!len) {
                return '';
            }
            let e = `<li data-bs-target="#${id}" data-bs-slide-to="${index}" class="ms-1 ${(active) ? 'active' : ''}"></li>`;
            return e + indicator(id, len - 1, false, index + 1);
        }

        let item = function (index, title, description, footer, link = false) {
            return `
            <!--begin::Item-->
            <div class="carousel-item ${(!index) ? 'active' : ''}">
                <!--begin::Wrapper-->
                <div class="carousel-wrapper">
                    <!--begin::Description-->
                    <div class="d-flex flex-column flex-grow-1">
                        <a href="#" class="fs-5 fw-bolder text-dark text-hover-primary">${title}</a>
                        <p class="text-gray-600 fs-6 fw-bold pt-3 mb-0 max-3-line">${description}</p>
                    </div>
                    <!--end::Description-->
                    <!--begin::Summary-->
                    <div class="d-flex flex-stack pt-8">
                        <span class="badge badge-light-primary fs-7 fw-bolder me-2">${footer}</span>
                        ${(link) ? `<a href="${link}" class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5">Xem Chi Tiết</a>` : ''}
                    </div>
                    <!--end::Summary-->
                </div>
                <!--end::Wrapper-->
            </div>
            <!--end::Item-->`
        }

        return `
            <!--begin::Heading-->
            <div class="d-flex flex-stack align-items-center flex-wrap">
                <h4 class="text-gray-400 fw-bolder text-uppercase mb-0 pe-2">${title}</h4>
                <!--begin::Carousel Indicators-->
                <ol class="p-0 m-0 carousel-indicators carousel-indicators-dots">
                    ${indicator(id, items.length)}
                </ol>
                <!--end::Carousel Indicators-->
            </div>
            <!--end::Heading-->
            <!--begin::Carousel inner-->
            <div class="carousel-inner pt-6">
                ${items.map((i, index) => item(index, i.title, i.description, i.footer, i.link)).join("")}
            </div>
            <!--end::Carousel inner-->
        `;
    },
    ServiceCard: function (name, link, icon) {
        name = name.replace("Tăng ", "");
        return `<div class="col-6">
            <div class="card card-stretch-50">
                <a href="${link}" class="btn btn-flex btn-text-gray-800 btn-icon-gray-400 btn-active-color-primary bg-body flex-column justfiy-content-start align-items-start text-start w-100 p-7">
                    <!--begin::Svg Icon | path: icons/duotune/ecommerce/ecm002.svg-->
                    <span class="svg-icon svg-icon-3x mb-5">
                        ${icon}
                    </span>
                    <!--end::Svg Icon-->
                    <span class="fs-5 fw-bolder max-1-line">${name}</span>
                </a>
            </div>
        </div>`
    },
    Breadcrumb: function (items) {
        let item = (title, link, active = false) => {
            let state = {
                true: `<li class="breadcrumb-item pe-md-3 pe-1"><a href="${link}" class="pe-md-3 pe-1">${title}</a></li>`,
                false: `<li class="breadcrumb-item px-md-3 px-1 text-muted">${title}</li>`
            }
            return state[active];
        }

        return `
            <ol class="breadcrumb breadcrumb-dot text-muted fs-6 fw-bold">
                ${items.map((i, index) => (index === items.length - 1) ? item(i.title, i.link, true) : item(i.title, i.link)).join("")}
            </ol>
        `;
    },
    facebookEmbed: (type, href, width=350) => {
        return `<div id="embed" class="fb-${type}" data-href="${href}" data-width="${width}"></div>`;
    },
    streamThumbnail: (user_id, display_name, live_title, home_point, verify, img, packages) => {
        let packages_ele = "";
        $.each(packages, (i, package) => {
            packages_ele += `<img class="mh-40px mh-40px mb-3" src="${(package.icon) ? package.icon : package.thumbnail}"/>`
        } )
        return `
        <div class="col-xl-2 col-xxl-2">
            <div class="card">
                <div class="position-absolute h-100 w-100 d-flex flex-column justify-content-between p-3 z-index-1 fw-boldest">
                    <div class="d-flex justify-content-between z-index-1 fw-boldest">
                        <div class="d-flex align-items-center">
                            <span class="badge badge-light-danger fs-9">
                                ${home_point}
                            </span>
                        </div>
                        <div>
                            <button class="btn btn-icon btn-sm btn-color-danger btn-active-color-primary me-n2" data-kt-menu-trigger="click"
                                    data-kt-menu-placement="bottom-end" data-kt-menu-overflow="true">
                                <!--begin::Svg Icon | path: icons/duotune/general/gen023.svg-->
                                <span class="svg-icon svg-icon-2">
									<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
										<rect opacity="0.3" x="2" y="2" width="20" height="20" rx="4" fill="black"></rect>
										<rect x="11" y="11" width="2.6" height="2.6" rx="1.3" fill="black"></rect>
										<rect x="15" y="11" width="2.6" height="2.6" rx="1.3" fill="black"></rect>
										<rect x="7" y="11" width="2.6" height="2.6" rx="1.3" fill="black"></rect>
									</svg>
								</span>
                                <!--end::Svg Icon-->
                            </button>
                            <div
                                class="menu menu-sub menu-sub-dropdown menu-column menu-rounded menu-gray-800 menu-state-bg-light-primary fw-bold w-200px py-3"
                                data-kt-menu="true" data-popper-placement="bottom-end"
                                style="z-index: 105; position: fixed; inset: 0px 0px auto auto; margin: 0px; transform: translate3d(-495px, 172px, 0px);">
                                <!--begin::Heading-->
                                <div class="menu-item px-3">
                                    <div class="menu-content text-muted pb-2 px-3 fs-7 text-uppercase">QUICK ACTIONS</div>
                                </div>
                                <!--end::Heading-->
                                <!--begin::Menu item-->
                                <div class="menu-item px-3">
                                    <a class="ban-stream menu-link px-3" data-user-id="${user_id}">Ban</a>
                                </div>
                                <!--end::Menu item-->
                                <!--begin::Menu item-->
                                <div class="menu-item px-3">
                                    <a class="delete-stream menu-link px-3" data-user-id="${user_id}">Delete</a>
                                </div>
                                <!--end::Menu item-->
                            </div>
                        </div>
                    </div>
                    <div class="d-flex flex-column align-items-end h-75">
                        ${packages_ele}
                    </div>
                    <div class="d-flex flex-column align-items-center z-index-1 fw-boldest">
                        <span class="mb-3 max-1-line">${live_title}</span>
                        <span class="max-1-line">${display_name}</span>
                        <span>
                            ${(verify) ? '<i class="idol_verify me-1"></i>' : ''}
                            ${user_id}
                        </span>
                    </div>
                </div>
                <div class="screenshot_gradient w-100 h-100 radius-5"></div>
                ${img}
            </div>
        </div>
        `
    }
}

const Formatter = {
    textShort: function (text, max = 10) {
        let re = new RegExp(`(.{${max}})..+`);
        return text.replace(re, "$1…").replace(' …', '…');
    },
    textUpper: function (text) {
        return String(text).toUpperCase();
    },
    textLower: function (text) {
        return String(text).toLowerCase();
    },
    numberComma: function (text) {
        return Number(text).toLocaleString();
    },
    unixString: function (unix, style = "full") {
        let a = new Date(Number(unix) * 1000);
        let year = a.getFullYear();
        let month = a.getMonth();
        let date = a.getDate();
        let hour = a.getHours();
        let min = a.getMinutes();
        let sec = a.getSeconds();
        let data = {
            "full": [year + '/' + Formatter.padFill(month, 2, 0) + '/' + Formatter.padFill(date, 2, 0), Formatter.padFill(hour, 2, 0) + ':' + Formatter.padFill(min, 2, 0) + ':' + Formatter.padFill(sec, 2, 0)],
            "short": `${date} Tháng ${month}, ${year}`
        }
        return data[style];
    },
    padFill: function (text, max, fill = " ") {
        return String(text).padStart(max, fill)
    },
    scale: (target, parent, scale = 0.5) => {
        target.css('-webkit-transform', 'scale('+scale+')');
        target.css('-webkit-transform-origin', 'top left');
        parent.width(parent.width() * scale);
        parent.height(parent.height() * scale);
    },
    indicatorToggle: (e, state=false) => {
        if (state){
            e.attr("data-kt-indicator", state);
            return;
        }
        (e.attr("data-kt-indicator")==="on") ? e.attr("data-kt-indicator", "off") : e.attr("data-kt-indicator", "on")
    },
    disabledToggle: (e, state) => {
        if (state){
            e.prop("disabled", state);
            return;
        }
        e.prop("disabled", !e.prop("disabled"));
    }
}

const Validator = {
    passwordStrong: (input) => {
        const value = input.value;
        if (value === '') {
            return {valid: true};
        }

        if (value.length < 8) {
            return {
                valid: false,
                message: 'Mật khẩu tối thiểu 8 ký tự',
            };
        }

        if (value === value.toLowerCase()) {
            return {
                valid: false,
                message: 'Phải bao gồm ít nhất 1 KÝ TỰ HOA từ A-Z',
            };
        }

        if (value === value.toUpperCase()) {
            return {
                valid: false,
                message: 'Phải bao gồm ít nhất 1 ký tự thường từ a-z',
            };
        }

        if (value.search(/[0-9]/) < 0) {
            return {
                valid: false,
                message: 'Phải bao gồm ít nhất 1 số từ 0-9',
            };
        }

        if (value.search(/(?=.*[!@#$%^&*()\-_=+])/) < 0) {
            return {
                valid: false,
                message: 'Phải bao gồm ít nhất 1 ký tự đặc biệt: !@#$%^&*()-_=+',
            };
        }

        return {valid: true};
    }
}

const Converter = {
    sha256: (ascii) => {
        function rightRotate(value, amount) {
            return (value >>> amount) | (value << (32 - amount));
        };

        let mathPow = Math.pow;
        let maxWord = mathPow(2, 32);
        let lengthProperty = 'length'
        let i, j;
        let result = ''
        let words = [];
        let asciiBitLength = ascii[lengthProperty] * 8;
        let hash = Converter.sha256.h = Converter.sha256.h || [];
        let k = Converter.sha256.k = Converter.sha256.k || [];
        let primeCounter = k[lengthProperty];
        let isComposite = {};
        for (let candidate = 2; primeCounter < 64; candidate++) {
            if (!isComposite[candidate]) {
                for (i = 0; i < 313; i += candidate) {
                    isComposite[i] = candidate;
                }
                hash[primeCounter] = (mathPow(candidate, .5) * maxWord) | 0;
                k[primeCounter++] = (mathPow(candidate, 1 / 3) * maxWord) | 0;
            }
        }
        ascii += '\x80'
        while (ascii[lengthProperty] % 64 - 56) ascii += '\x00'
        for (i = 0; i < ascii[lengthProperty]; i++) {
            j = ascii.charCodeAt(i);
            if (j >> 8) return;
            words[i >> 2] |= j << ((3 - i) % 4) * 8;
        }
        words[words[lengthProperty]] = ((asciiBitLength / maxWord) | 0);
        words[words[lengthProperty]] = (asciiBitLength)

        for (j = 0; j < words[lengthProperty];) {
            let w = words.slice(j, j += 16);
            let oldHash = hash;
            hash = hash.slice(0, 8);

            for (i = 0; i < 64; i++) {
                let i2 = i + j;
                let w15 = w[i - 15], w2 = w[i - 2];
                let a = hash[0], e = hash[4];
                let temp1 = hash[7]
                    + (rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25)) // S1
                    + ((e & hash[5]) ^ ((~e) & hash[6])) // ch
                    + k[i]
                    + (w[i] = (i < 16) ? w[i] : (
                            w[i - 16]
                            + (rightRotate(w15, 7) ^ rightRotate(w15, 18) ^ (w15 >>> 3)) // s0
                            + w[i - 7]
                            + (rightRotate(w2, 17) ^ rightRotate(w2, 19) ^ (w2 >>> 10)) // s1
                        ) | 0
                    );
                let temp2 = (rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22)) // S0
                    + ((a & hash[1]) ^ (a & hash[2]) ^ (hash[1] & hash[2])); // maj

                hash = [(temp1 + temp2) | 0].concat(hash); // We don't bother trimming off the extra ones, they're harmless as long as we're truncating when we do the slice()
                hash[4] = (hash[4] + temp1) | 0;
            }

            for (i = 0; i < 8; i++) {
                hash[i] = (hash[i] + oldHash[i]) | 0;
            }
        }

        for (i = 0; i < 8; i++) {
            for (j = 3; j + 1; j--) {
                let b = (hash[i] >> (j * 8)) & 255;
                result += ((b < 16) ? 0 : '') + b.toString(16);
            }
        }
        return result;
    }
}

toastr.options = {
      "closeButton": true,
      "debug": false,
      "newestOnTop": true,
      "progressBar": true,
      "positionClass": "toast-top-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
};

const popup = {
    mini: {
        success: (message, title="") => {
            (title) ? toastr.success(message, title) : toastr.success(message)
        },
        error: (message, title) => {
            (title) ? toastr.error(message, title) : toastr.error(message)
        },
        info: (message, title) => {
            (title) ? toastr.info(message, title) : toastr.success(message)
        },
        warning: (message, title) => {
            (title) ? toastr.warning(message, title) : toastr.warning(message)
        },
    },
    large: {
        success: (message) => {
            Swal.fire({
                text: message,
                icon: "success",
                buttonsStyling: false,
                confirmButtonText: "Tắt",
                customClass: {
                    confirmButton: "btn btn-primary"
                }
            });
        },
        error: (message) => {
            Swal.fire({
                text: message,
                icon: "error",
                buttonsStyling: false,
                confirmButtonText: "Tắt",
                customClass: {
                    confirmButton: "btn btn-primary"
                }
            });
        }
    }
}

const updateElement = {
    notification: (read_all = true) => {
        if (read_all) {
            $(".notification").each(function () {
                $(this).removeClass('border-primary').addClass('border-gray-300');
                let bullet = $(this).find(".bullet");
                (bullet) ? bullet.remove() : '';
            })
            $("a[data-kt-drawer-target='#kt_notification']").each(function () {
                let bullet = $(this).find(".bullet");
                (bullet) ? bullet.remove() : '';
            })
        }
    },
    loadMoreNotification: (e) => {
        $("#notifications").append($(e).hide().fadeIn(2000));
    },
    data: (query, data, value, delay = 0) => {
        setTimeout(() => {
            query.attr('data-' + data, value);
        }, delay);
    }
}

const pageReady = (done=true, uncover=true) => {
    if (uncover) {
        $("#page_loading").fadeOut().addClass('invisible');
        $("#loader").addClass('invisible');
    }
    if (done) {
        $(NProgress.settings.barSelector).fadeOut(1000);
        setTimeout(() => {
            NProgress.done(true)
        }, 1000);
    }
}

$("#notification_read_all").click(function () {
    let button = $(this);
    let n = Array()
    $(".notification").each(function () {
        n.push($(this).data('id'));
    })
    $.ajax({
        type: 'POST',
        url: '/notification/mark_read',
        dataType: 'json',
        headers: {
            'X-CSRF-TOKEN': getCookie('csrf_access_token'),
        },
        data: {'id': JSON.stringify(n)},
        beforeSend: function () {
            updateElement.data(button, "kt-indicator", "on");
        },
        success: function (data) {
            updateElement.notification(true);
            $("#notification_unread").html("Hiện không có thông báo mới");
            updateElement.data(button, "kt-indicator", "off", 500);
        },
        error: function (xhr) {
        },
    });
});

$("#older_notifications").click(function () {
    let button = $(this);
    $.ajax({
        type: 'GET',
        url: '/notification',
        dataType: 'json',
        data: {'after': $(".notification").last().data('id')},
        beforeSend: function () {
            updateElement.data(button, "kt-indicator", "on");
        },
        success: function (data) {
            updateElement.data(button, "kt-indicator", "off");
            if (data['data']) {
                updateElement.loadMoreNotification(data['data']);
            } else {
                button.find(".indicator-label").text("Đã tải toàn bộ thông báo");
                button.removeClass('btn-primary').addClass('btn-bg-light').unbind("click");
            }
        },
        error: function (xhr) {
        },
    });
});

$(window).on("beforeunload", function () {
    $("#page_loading").removeClass('invisible').fadeIn();
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

const screenBreakpoint = () => {
    let w = $(document).innerWidth();
    return (w < 768) ? 'xs' : ((w < 992) ? 'sm' : ((w < 1200) ? 'md' : 'lg'));
};