const BOOKMARK_KEY = "projecthub-django-bookmarks";

function getBookmarks() {
    try {
        return JSON.parse(localStorage.getItem(BOOKMARK_KEY)) || [];
    } catch {
        return [];
    }
}

function saveBookmarks(bookmarks) {
    localStorage.setItem(BOOKMARK_KEY, JSON.stringify(bookmarks));
}

function updateBookmarkButtons() {
    const bookmarks = getBookmarks();

    document.querySelectorAll("[data-bookmark-button]").forEach((button) => {
        const postId = String(button.dataset.postId);
        const saved = bookmarks.includes(postId);

        button.textContent = saved ? "★ Bookmarked" : "☆ Bookmark";
    });

    const headerButton = document.getElementById("bookmark-view-button");

    if (headerButton) {
        headerButton.textContent =
            `★ Bookmarks (${bookmarks.length})`;
    }
}

document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll("[data-bookmark-button]").forEach((button) => {
        button.addEventListener("click", () => {

            const postId = String(button.dataset.postId);
            let bookmarks = getBookmarks();

            if (bookmarks.includes(postId)) {
                bookmarks = bookmarks.filter((id) => id !== postId);
            } else {
                bookmarks.push(postId);
            }

            saveBookmarks(bookmarks);
            updateBookmarkButtons();
        });
    });

    updateBookmarkButtons();
});
