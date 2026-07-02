
    function changeTheme(themeName) {
        document.body.className = themeName;
    }


    function changeTheme(themeName) {
        // Set a cookie that expires in 30 days
        document.cookie = "theme=" + themeName + "; path=/; max-age=" + (60 * 60 * 24 * 30);

        // Apply the theme class immediately
        document.body.className = themeName;
    }

    // On page load, apply the theme from the cookie
    window.onload = function () {
        const cookies = document.cookie.split(';');
        let theme = 'theme-default';  // fallback

        for (let i = 0; i < cookies.length; i++) {
            const [name, value] = cookies[i].trim().split('=');
            if (name === 'theme') {
                theme = value;
                break;
            }
        }

        document.body.className = theme;
    };

