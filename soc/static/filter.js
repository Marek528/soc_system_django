document.addEventListener('DOMContentLoaded', () => {
    const konzultantSelect = document.querySelector('#konzultant-form');
    const odborSelect = document.querySelector('#odbor-form');
    const dostupnostSelect = document.querySelector('#dostupnost-form');
    const themes = document.querySelectorAll('.tema');

    function filterThemes() {
        const konzultantFilter = konzultantSelect.value;
        const odborFilter = odborSelect.value;
        const dostupnostFilter = dostupnostSelect.value;

        themes.forEach((item) => {
            const konzultant = item.querySelector('.tema-konzultant').dataset.konzultant;
            const odbor = item.querySelector('.tema-odbor').dataset.odbor;
            const dostupnost = item.querySelector('.tema-dostupnost').dataset.dostupnost;

            const konzultantMatch = konzultantFilter === "" || konzultantFilter === konzultant;
            const odborMatch = odborFilter === "" || odborFilter === odbor;
            const dostupnostMatch = dostupnostFilter === "" || dostupnostFilter === dostupnost;

            if (konzultantMatch && odborMatch && dostupnostMatch) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
    }

    konzultantSelect.addEventListener('change', filterThemes);
    odborSelect.addEventListener('change', filterThemes);
    dostupnostSelect.addEventListener('change', filterThemes);
});