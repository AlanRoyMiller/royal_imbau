const contactForm = document.querySelectorAll('#contact-form .error');



Array.from(contactForm).forEach(form => {
    let upperSibling = form.previousElementSibling;
    upperSibling.classList.add('box');


    upperSibling.addEventListener('click', function (e) {
        form.parentElement.removeChild(form);
    });
});


if (window.location.search.includes('submitted=True')) {
    const messageElement = document.getElementById('form-response');
    const titleElement = document.getElementById('form-title');

    titleElement.style.display = 'none';
    if (currentPath.startsWith("/es")) {
        messageElement.textContent = 'Gracias por tu mensaje. ¡Nos pondremos en contacto pronto!';
    } else if (currentPath.startsWith("/de")) {
        messageElement.textContent = 'Vielen Dank für Ihre Nachricht. Wir werden uns bald bei Ihnen melden!';
    } else {
        messageElement.textContent = 'Thank you for your message. We will be in touch soon!';
    }
    messageElement.style.display = 'block';
}