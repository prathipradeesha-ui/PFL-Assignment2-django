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
        const showingBookmarks =
            headerButton.getAttribute("data-view") === "bookmarks";

        headerButton.textContent = showingBookmarks
            ? "← All Posts"
            : `★ Bookmarks (${bookmarks.length})`;
    }
}

function updateVisiblePosts() {
    const headerButton = document.getElementById("bookmark-view-button");

    if (!headerButton) {
        return;
    }

    const showingBookmarks =
        headerButton.getAttribute("data-view") === "bookmarks";

    const bookmarks = getBookmarks();
    const postCards = document.querySelectorAll("[data-post-card]");
    const emptyMessage = document.getElementById("no-bookmarked-posts");

    let visibleCount = 0;

    postCards.forEach((card) => {
        const postId = String(card.dataset.postId);
        const shouldShow = !showingBookmarks || bookmarks.includes(postId);

        card.style.display = shouldShow ? "" : "none";

        if (shouldShow) {
            visibleCount += 1;
        }
    });

    if (emptyMessage) {
        emptyMessage.style.display =
            showingBookmarks && visibleCount === 0 ? "" : "none";
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
            updateVisiblePosts();
        });
    });

    const headerButton = document.getElementById("bookmark-view-button");

    if (headerButton) {
        headerButton.setAttribute("data-view", "all");

        headerButton.addEventListener("click", () => {
            const currentView = headerButton.getAttribute("data-view");

            headerButton.setAttribute(
                "data-view",
                currentView === "bookmarks" ? "all" : "bookmarks"
            );

            updateBookmarkButtons();
            updateVisiblePosts();
        });
    }

    updateBookmarkButtons();
});
