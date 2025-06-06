// Language selector function
document.getElementById("languages").onchange = function() {
    const selectedLanguage = this.value;

    // Get the current page's path
    const currentPath = window.location.pathname;

    // Get the new path for the selected language
    const newPath = getNewPath(currentPath, selectedLanguage);

    // Redirect to the new URL
    window.location.href = newPath;
}

// Function to get the new path for the selected language
function getNewPath(currentPath, selectedLanguage) {
    const homepage = { "english": "/", "spanish": "/es/", "german": "/de/" };
    const about = { "english": "/about/", "spanish": "/es/about/", "german": "/de/about/" };
    const gallery = { "english": "/gallery/", "spanish": "/es/gallery/", "german": "/de/gallery/" };
    const contact = { "english": "/#contact-us/", "spanish": "/es/#contact-us/", "german": "/de/#contact-us/" };

    const pathMappings = {
        "/": homepage,
        "/about/": about,
        "/gallery/": gallery,
        "/#contact-us/": contact,
        "/es/": homepage,
        "/es/about/": about,
        "/es/gallery/": gallery,
        "/es/#contact-us/": contact,
        "/de/": homepage,
        "/de/about/": about,
        "/de/gallery/": gallery,
        "/de/#contact-us/": contact
    };

    const mappings = pathMappings[currentPath];
    if (mappings) {
        return mappings[selectedLanguage];
    }

    // If the current path is not found in the mappings, return the main page for the selected language
    switch(selectedLanguage) {
        case "english":
            return "/";
        case "spanish":
            return "/es/";
        case "german":
            return "/de/"; 
    }
}

// Set the default language based on the current URL
const currentPathForDefault = window.location.pathname;

if (currentPathForDefault.startsWith("/es")) {
    document.getElementById("languages").value = "spanish";
} else if (currentPathForDefault.startsWith("/de")) {
    document.getElementById("languages").value = "german";
} else {
    document.getElementById("languages").value = "english";
}