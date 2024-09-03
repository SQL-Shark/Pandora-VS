import wixUsers from 'wix-users';
import wixWindow from "wix-window";
import { session } from 'wix-storage';

$w.onReady(() => {
    console.log("Page is ready");

    // Check if the user is logged in
    if (!wixUsers.currentUser.loggedIn) {
        console.log("User is not logged in");

        // Check if the lightbox has already been shown
        if (!session.getItem('lightboxShown')) {
            console.log("Opening lightbox");
            wixWindow.openLightbox('Subscribe');
            session.setItem('lightboxShown', 'true');
        } else {
            console.log("Lightbox already shown");
        }
    } else {
        console.log("User is logged in");
    }
});