const BASE_URL = "https://property-rental-system-using-jwt-and.onrender.com";

const API = {
    // Session state retrieval
    getToken() {
        return localStorage.getItem("token");
    },
    
    getUserEmail() {
        return localStorage.getItem("userEmail");
    },

    // Request Helper
    async request(endpoint, method = "GET", data = null) {
        const token = this.getToken();
        const headers = {
            "Content-Type": "application/json"
        };
        
        if (token) {
            headers["Authorization"] = `Bearer ${token}`;
        }

        const config = {
            method,
            headers
        };

        if (data) {
            config.body = JSON.stringify(data);
        }

        try {
            const response = await fetch(`${BASE_URL}${endpoint}`, config);
            
            // Redirect to Login if session expires or unauthorized
            if (response.status === 401) {
                this.logout();
                window.location.href = "index.html";
                return null;
            }

            if (!response.ok) {
                const err = await response.json().catch(() => ({}));
                throw new Error(err.detail || `HTTP Error ${response.status}`);
            }

            // For DELETE calls or empty bodies that return JSON messages
            return await response.json();
        } catch (error) {
            console.error(`API Error at ${endpoint}:`, error);
            throw error; // Rethrow to let the UI display the alert
        }
    },

    // Authentication
    async login(email, password) {
        try {
            const response = await fetch(`${BASE_URL}/auth/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email, password })
            });

            if (!response.ok) {
                const err = await response.json().catch(() => ({}));
                throw new Error(err.detail || "Invalid email or password.");
            }

            const data = await response.json();
            localStorage.setItem("token", data.access_token);
            localStorage.setItem("userEmail", email);
            return data;
        } catch (error) {
            console.error("Login Error:", error);
            throw error;
        }
    },

    logout() {
        localStorage.removeItem("token");
        localStorage.removeItem("userEmail");
        window.location.href = "index.html";
    },

    // Properties CRUD
    getProperties() {
        return this.request("/properties/");
    },

    addProperty(title, location, price) {
        return this.request("/properties/", "POST", { title, location, price });
    },

    deleteProperty(id) {
        return this.request(`/properties/${id}`, "DELETE");
    },

    // Tenants CRUD
    getTenants() {
        return this.request("/tenants/");
    },

    addTenant(name, email, phone) {
        return this.request("/tenants/", "POST", { name, email, phone });
    },

    // Agreements CRUD
    getAgreements() {
        return this.request("/agreements/");
    },

    addAgreement(property_id, tenant_id, rent) {
        return this.request("/agreements/", "POST", { property_id, tenant_id, rent });
    },

    // Payments CRUD
    getPayments() {
        return this.request("/payments/");
    },

    addPayment(agreement_id, amount, status) {
        return this.request("/payments/", "POST", { agreement_id, amount, status });
    }
};
