/* ==========================================================================
   Coaching Management System - Client-side JS
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {
    initSidebarToggle();
    initAutoDismissAlerts();
    initDeleteConfirmations();
    initFormValidation();
});

/**
 * Toggle the sidebar on small screens.
 */
function initSidebarToggle() {
    const toggleBtn = document.getElementById('menuToggle');
    const sidebar = document.querySelector('.sidebar');

    if (!toggleBtn || !sidebar) {
        return;
    }

    toggleBtn.addEventListener('click', function () {
        sidebar.classList.toggle('open');
    });

    document.addEventListener('click', function (event) {
        const isClickInsideSidebar = sidebar.contains(event.target);
        const isClickOnToggle = toggleBtn.contains(event.target);

        if (!isClickInsideSidebar && !isClickOnToggle) {
            sidebar.classList.remove('open');
        }
    });
}

/**
 * Auto-dismiss success/error alert messages after a few seconds.
 */
function initAutoDismissAlerts() {
    const alerts = document.querySelectorAll('.alert');

    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = 'opacity 0.4s ease';
            alert.style.opacity = '0';
            setTimeout(function () {
                alert.remove();
            }, 400);
        }, 4000);
    });
}

/**
 * Ask for confirmation before submitting any "delete" forms,
 * as an extra safety net on top of the confirm_delete page.
 */
function initDeleteConfirmations() {
    const deleteForms = document.querySelectorAll('form[data-confirm]');

    deleteForms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
            const message = form.getAttribute('data-confirm') || 'Are you sure?';
            if (!window.confirm(message)) {
                event.preventDefault();
            }
        });
    });
}

/**
 * Lightweight client-side validation: highlight empty required fields
 * before allowing the form to submit, improving UX before the
 * server-side Django validation runs.
 */
function initFormValidation() {
    const forms = document.querySelectorAll('form.login-form, .form-card form');

    forms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
            let hasError = false;
            const requiredFields = form.querySelectorAll('input[required], select[required]');

            requiredFields.forEach(function (field) {
                clearFieldError(field);

                if (!field.value.trim()) {
                    hasError = true;
                    showFieldError(field, 'This field is required.');
                }
            });

            if (hasError) {
                event.preventDefault();
            }
        });

        form.querySelectorAll('input, select, textarea').forEach(function (field) {
            field.addEventListener('input', function () {
                clearFieldError(field);
            });
        });
    });
}

function showFieldError(field, message) {
    field.classList.add('input-error');

    let errorEl = field.parentElement.querySelector('.js-field-error');
    if (!errorEl) {
        errorEl = document.createElement('span');
        errorEl.className = 'field-error js-field-error';
        field.parentElement.appendChild(errorEl);
    }
    errorEl.textContent = message;
}

function clearFieldError(field) {
    field.classList.remove('input-error');
    const errorEl = field.parentElement.querySelector('.js-field-error');
    if (errorEl) {
        errorEl.remove();
    }
}
