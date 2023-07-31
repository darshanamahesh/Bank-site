document.addEventListener('DOMContentLoaded', function() {
  const districtSelect = document.querySelector('.district-select');
  const branchSelect = document.querySelector('.branch-select');

  // Function to fetch branch options based on selected district
  function fetchBranches() {
    const districtId = districtSelect.value;
    fetch(`/api/branches/${districtId}`)
      .then(response => response.json())
      .then(data => {
        branchSelect.innerHTML = '';
        data.forEach(branch => {
          const option = new Option(branch.name, branch.id);
          branchSelect.add(option);
        });
      });
  }

  // Fetch branch options when the page loads and whenever district selection changes
  fetchBranches();
  districtSelect.addEventListener('change', fetchBranches);
});
