import {RelativeTimeElement} from "@github/relative-time-element";
import Alpine from 'alpinejs';
import Swiper from 'swiper';
import { Autoplay, Navigation, Pagination } from 'swiper/modules';
import 'swiper/css';
import CustomToast from "./js/toast";
import './css/urls.css';

window.htmx = require('htmx.org');

document.addEventListener('display_toast', (e) => {
  CustomToast({template_id:"toast-template", data:e.detail})
});

document.addEventListener("DOMContentLoaded", () => {
    window.Alpine = Alpine;
    Alpine.start();

    const progressCircle = document.querySelector(".autoplay-progress svg");
    const progressContent = document.querySelector(".autoplay-progress span");

    const swiper = new Swiper('#testimonial-wrapper', {
        modules: [Autoplay, Navigation, Pagination],

        // Optional parameters
        loop: true,
        speed: 1000,

        slidesPerView: 1,
        spaceBetween: 10,
        breakpoints: {
            768: {
              slidesPerView: 2,
              spaceBetween: 20
            },
        },
        autoplay: {
            delay: 4000,
            disableOnInteraction: false,
        },
        on: {
            autoplayTimeLeft(s, time, progress) {
              progressCircle.style.setProperty("--progress", 1 - progress);
              progressContent.textContent = `${Math.ceil(time / 1000)}s`;
            }
          }

    });
    
});