document.addEventListener("DOMContentLoaded", function () {
    const stockList = document.getElementById("stock-list");
    const topNInput = document.getElementById("top-n");
    const submitButton = document.getElementById("submit-btn");
    const smallestButton = document.getElementById("smallest-btn");

    let currentFetchType = null; 
    let currentTopN = 0;         
    let refreshInterval = null; 

   
    function fetchStocks(type, topN) {
        const endpoint = type === "top" ? `/top-stocks/${topN}` : `/smallest-stocks/${topN}`;
        fetch(endpoint)
            .then(response => response.json())
            .then(stocks => {
                stockList.innerHTML = "";
                stocks.forEach(stock => createStockCard(stock));
            })
            .catch(error => console.error(`Error fetching ${type} stocks:`, error));
    }

   
    function createStockCard(stock) {
        const card = document.createElement("div");
        card.className = "col-md-4";
        card.innerHTML = `
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${stock.symbol}</h5>
                    <p class="card-text">Price: ₹${stock.performance}</p>
                    <div class="canvas-container">
                        <canvas id="chart-${stock.symbol}"></canvas>
                    </div>
                </div>
            </div>
        `;
        stockList.appendChild(card);

      
        const ctx = document.getElementById(`chart-${stock.symbol}`).getContext("2d");
        new Chart(ctx, {
            type: "line",
            data: {
                labels: [1, 2, 3, 4, 5], 
                datasets: [{
                    label: "Performance",
                    data: [stock.performance - 2, stock.performance - 1, stock.performance, stock.performance + 1, stock.performance + 2],
                    borderColor: "#17a2b8",
                    fill: false,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { display: false },
                    y: { display: false }
                },
                plugins: {
                    legend: { display: false }
                }
            }
        });
    }

  
    function startAutoRefresh(type, topN) {
        if (refreshInterval) clearInterval(refreshInterval); 
        refreshInterval = setInterval(() => fetchStocks(type, topN), 10000);
    }

    
    submitButton.addEventListener("click", function () {
        const topN = parseInt(topNInput.value);

        if (topN && topN > 0) {
            currentFetchType = "top";
            currentTopN = topN;
            fetchStocks("top", topN);
            startAutoRefresh("top", topN); 
        } else {
            alert("Please enter a valid number greater than 0.");
        }
    });

    
    smallestButton.addEventListener("click", function () {
        const topN = parseInt(topNInput.value);

        if (topN && topN > 0) {
            currentFetchType = "smallest";
            currentTopN = topN;
            fetchStocks("smallest", topN); 
            startAutoRefresh("smallest", topN); 
        } else {
            alert("Please enter a valid number greater than 0.");
        }
    });
});
