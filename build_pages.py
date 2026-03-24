import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TITLE_VAR - Insurance Package Network</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="style.css">
</head>
<body class="bg-light">
    <!-- Topbar -->
    <div class="topbar position-relative z-3">
        <div class="container d-flex justify-content-between align-items-center py-2">
            <div class="contact-info text-white">
                <span class="me-4"><i class="fas fa-phone-alt me-2"></i>+0123 456 789</span>
            </div>
            <div class="social-icons">
                <span class="text-white"><i class="fas fa-envelope me-2 text-white"></i>info@domain.com</span>
            </div>
        </div>
    </div>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg bg-white sticky-top py-3 shadow-sm z-3">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="index.html">
                <div class="logo-icon me-2 position-relative">
                    <img src="https://api.iconify.design/fluent:people-community-24-filled.svg?color=%23002b61" width="45" height="45" alt="Logo">
                </div>
                <div>
                    <span class="fw-bold fs-4 d-block lh-1 text-dark">Insurance Package Network</span>
                    <span class="fs-6 logo-subtitle">Insurance Agency</span>
                </div>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto fw-medium">
                    <li class="nav-item px-2"><a class="nav-link text-secondary" href="index.html">Home</a></li>
                    <li class="nav-item px-2"><a class="nav-link text-secondary" href="index.html">About us</a></li>
                    <li class="nav-item px-2"><a class="nav-link text-dark fw-semibold" href="index.html">Services</a></li>
                    <li class="nav-item px-2 dropdown">
                        <a class="nav-link dropdown-toggle text-secondary" href="#" role="button" data-bs-toggle="dropdown">Pages</a>
                    </li>
                    <li class="nav-item px-2"><a class="nav-link text-secondary" href="index.html">Our Team</a></li>
                </ul>
                <a href="#" class="btn btn-primary btn-custom px-4 py-2 fw-medium">Contact Us</a>
            </div>
        </div>
    </nav>

    <!-- Inner Hero -->
    <section class="page-header py-5 position-relative bg-primary overflow-hidden">
       <div class="position-absolute top-0 start-0 w-100 h-100 z-0 bg-pattern-blue"></div>
       <div class="container py-5 mt-4 text-center position-relative z-1 text-white">
           <span class="badge badge-custom px-4 py-2 mb-4 rounded-pill fw-medium fs-6 bg-white text-primary shadow-sm border border-light">Insurance Package Network Protection</span>
           <h1 class="display-4 fw-bold mb-3">TITLE_VAR</h1>
           <nav aria-label="breadcrumb">
               <ol class="breadcrumb justify-content-center mb-0 mt-3">
                   <li class="breadcrumb-item"><a href="index.html" class="text-white text-decoration-none opacity-75 fw-medium">Home</a></li>
                   <li class="breadcrumb-item"><a href="index.html" class="text-white text-decoration-none opacity-75 fw-medium">Services</a></li>
                   <li class="breadcrumb-item active text-white fw-bold" aria-current="page">TITLE_VAR</li>
               </ol>
           </nav>
       </div>
    </section>

    <!-- Main Content -->
    <section class="service-details py-5 my-3 my-lg-2">
       <div class="container py-lg-4">
           <div class="row g-5">
               <div class="col-lg-8">
                   <div class="position-relative mb-5 rounded-4 shadow-sm w-100 overflow-hidden" style="height: 480px;">
                       <img src="IMG_VAR" class="w-100 h-100 object-fit-cover hover-scale" alt="TITLE_VAR" style="transition: transform 0.8s ease;">
                   </div>
                   
                   <h2 class="fw-bold text-dark mb-4 fs-1" style="letter-spacing: -1px;">TITLE_VAR Overview</h2>
                   <div class="mb-5 pb-2">
                       <p class="text-secondary lh-lg mb-4 fs-6">DESC_1_VAR</p>
                       <p class="text-secondary lh-lg mb-0 fs-6">DESC_2_VAR</p>
                   </div>
                   
                   <div class="bg-white rounded-4 p-4 p-md-5 mb-4 shadow-sm border border-light border-2">
                       <h3 class="fw-bold text-dark mb-4 pb-2 border-bottom border-light">What's Covered inside the Policy?</h3>
                       <ul class="list-unstyled mb-0 row gx-4 gy-4">
                           <li class="col-md-6 d-flex align-items-start"><i class="fas fa-check-circle text-primary mt-1 me-3 fs-4"></i><span class="text-secondary lh-base fw-medium">COV_1_VAR</span></li>
                           <li class="col-md-6 d-flex align-items-start"><i class="fas fa-check-circle text-primary mt-1 me-3 fs-4"></i><span class="text-secondary lh-base fw-medium">COV_2_VAR</span></li>
                           <li class="col-md-6 d-flex align-items-start"><i class="fas fa-check-circle text-primary mt-1 me-3 fs-4"></i><span class="text-secondary lh-base fw-medium">COV_3_VAR</span></li>
                           <li class="col-md-6 d-flex align-items-start"><i class="fas fa-check-circle text-primary mt-1 me-3 fs-4"></i><span class="text-secondary lh-base fw-medium">COV_4_VAR</span></li>
                       </ul>
                   </div>
               </div>
               
               <!-- Sidebar -->
               <div class="col-lg-4">
                   <div class="card border border-light border-2 bg-white shadow-sm rounded-4 p-4 p-xl-5 mb-4 position-sticky" style="top: 120px;">
                       <h4 class="fw-bold text-dark mb-4 border-bottom border-light pb-3">Other Services</h4>
                       <ul class="list-unstyled mb-5 feature-list">
                           <li class="mb-3 border-bottom border-light pb-3"><a href="home-insurance.html" class="text-decoration-none text-secondary fw-semibold d-flex align-items-center custom-hover-text"><i class="fas fa-angle-right me-3 text-primary"></i>Home Insurance</a></li>
                           <li class="mb-3 border-bottom border-light pb-3"><a href="tenant-insurance.html" class="text-decoration-none text-secondary fw-semibold d-flex align-items-center custom-hover-text"><i class="fas fa-angle-right me-3 text-primary"></i>Tenant Insurance</a></li>
                           <li class="mb-3 border-bottom border-light pb-3"><a href="vehicle-insurance.html" class="text-decoration-none text-secondary fw-semibold d-flex align-items-center custom-hover-text"><i class="fas fa-angle-right me-3 text-primary"></i>Vehicle Insurance</a></li>
                           <li class="mb-3 border-bottom border-light pb-3"><a href="property-insurance.html" class="text-decoration-none text-secondary fw-semibold d-flex align-items-center custom-hover-text"><i class="fas fa-angle-right me-3 text-primary"></i>Property Insurance</a></li>
                           <li class="mb-3 border-bottom border-light pb-3"><a href="business-insurance.html" class="text-decoration-none text-secondary fw-semibold d-flex align-items-center custom-hover-text"><i class="fas fa-angle-right me-3 text-primary"></i>Business Insurance</a></li>
                           <li class="pt-1"><a href="travel-insurance.html" class="text-decoration-none text-secondary fw-semibold d-flex align-items-center custom-hover-text"><i class="fas fa-angle-right me-3 text-primary"></i>Travel Insurance</a></li>
                       </ul>
                       
                       <div class="card border-0 bg-primary text-white rounded-4 p-4 p-xl-4 text-center position-relative overflow-hidden mt-2 shadow-lg">
                           <div class="position-absolute top-0 start-0 w-100 h-100 bg-pattern-blue opacity-50 z-0"></div>
                           <i class="fas fa-headset fa-3x mb-4 text-white position-relative z-1 mt-4"></i>
                           <h4 class="fw-bold text-white mb-3 position-relative z-1">Need Insurance Help?</h4>
                           <p class="text-white opacity-75 small mb-4 px-2 position-relative z-1 lh-lg">Reach out to our experts for a customized quote tailored perfectly to your immediate needs.</p>
                           <a href="#" class="btn btn-white text-primary fw-bold rounded-pill w-100 py-3 mb-4 position-relative z-1 shadow custom-hover-lift">Get a Quote</a>
                           <div class="position-relative z-1 mb-2">
                               <span class="fw-bold text-white fs-5"><i class="fas fa-phone-alt me-2"></i>+0123 456 789</span>
                           </div>
                       </div>
                   </div>
               </div>
           </div>
       </div>
    </section>

    <!-- Footer Area (CTA block from index.html) -->
    <section class="cta-section py-5 position-relative overflow-hidden bg-white mt-auto border-top border-light border-3">
        <div class="floating-elements position-absolute top-0 start-0 w-100 h-100 z-0 opacity-75">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Avatar" class="position-absolute rounded-circle shadow-sm float-avatar" style="width: 55px; height: 55px; top: 20%; left: 8%; animation-delay: 0s;">
            <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Avatar" class="position-absolute rounded-circle shadow-sm float-avatar" style="width: 65px; height: 65px; top: 55%; left: 15%; animation-delay: 1s;">
            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Avatar" class="position-absolute rounded-circle shadow-sm float-avatar d-none d-md-block" style="width: 45px; height: 45px; top: 80%; left: 25%; animation-delay: 2s;">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Avatar" class="position-absolute rounded-circle shadow-sm float-avatar" style="width: 50px; height: 50px; top: 15%; right: 15%; animation-delay: 1.5s;">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Avatar" class="position-absolute rounded-circle shadow-sm float-avatar" style="width: 60px; height: 60px; top: 65%; right: 10%; animation-delay: 0.5s;">
            <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Avatar" class="position-absolute rounded-circle shadow-sm float-avatar d-none d-md-block" style="width: 55px; height: 55px; top: 85%; right: 28%; animation-delay: 2.5s;">
            <span class="position-absolute rounded-circle float-dot" style="width: 30px; height: 30px; background-color: #ff8c42; top: 45%; left: 8%; animation-delay: 1.2s;"></span>
            <span class="position-absolute rounded-circle float-dot" style="width: 40px; height: 40px; background-color: var(--primary-color); top: 30%; right: 22%; animation-delay: 0.3s;"></span>
        </div>

        <div class="container position-relative z-1 py-5 text-center" style="max-width: 850px;">
            <h6 class="text-primary fw-bold text-uppercase mb-3" style="letter-spacing: 1px; font-size: 0.85rem;">You're in good company</h6>
            <h2 class="display-6 fw-bold text-dark mb-5 lh-sm px-md-4" style="letter-spacing: -0.5px;">Join over 3,000,000 customers who received insurance quotes from us</h2>
            
            <div class="input-group input-group-lg mb-4 shadow-sm mx-auto cta-input-group" style="max-width: 650px;">
                <input type="text" class="form-control border-light bg-light px-4 fs-6" placeholder="Enter your email address" aria-label="Email address">
                <button class="btn btn-primary fw-bold text-uppercase px-4 px-md-5 fs-6 d-flex align-items-center justify-content-center" type="button">
                    <i class="fas fa-shield-alt me-2"></i> Get a quote
                </button>
            </div>
            
            <p class="mb-3 fw-medium text-secondary">Find out how affordable personalized insurance can be in 5 minutes with an online quote.</p>
            <p class="small text-secondary mb-5 pb-4 border-bottom border-light">Before you start, please review our <a href="#" class="text-primary text-decoration-none fw-medium">Privacy Policy</a> and <a href="#" class="text-primary text-decoration-none fw-medium">Terms of Use</a>.</p>
            
            <div class="mt-4">
                <p class="small text-secondary mb-0">&copy; 2026 Insurance Package Network. All Rights Reserved.</p>
            </div>
        </div>
    </section>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""

pages = [
    {
        "filename": "home-insurance.html",
        "title": "Home Insurance",
        "img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "desc1": "Your home is more than just a building; it's where your life happens. Our comprehensive Home Insurance plans are designed to protect your most valuable asset from unforeseen events such as severe weather, fires, theft, and vandalism. We offer flexible coverage limits that ensure your dwelling, personal belongings, and additional structures are completely secure.",
        "desc2": "Besides covering physical damage, our policies include robust personal liability protection. This ensures that if someone is injured on your property, your legal and medical expenses are covered without draining your life savings. Sleep soundly knowing that your sanctuary is fully guarded by Insurance Package Network.",
        "cov1": "Dwelling Protection against fire, wind, and hail",
        "cov2": "Personal Property Coverage for theft or damage",
        "cov3": "Liability Protection for visitor injuries",
        "cov4": "Additional Living Expenses during home repairs"
    },
    {
        "filename": "tenant-insurance.html",
        "title": "Tenant Insurance",
        "img": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "desc1": "Renting an apartment or house comes with its own unique set of risks. Your landlord's insurance covers the building, but it absolutely does not cover your personal belongings. Tenant Insurance (or Renter's Insurance) is a highly affordable way to protect your furniture, electronics, clothing, and valuables from theft, fire, and water damage.",
        "desc2": "In the event that a covered disaster makes your rented home temporarily unlivable, our Tenant Insurance policy will cover the costs of a hotel and additional living expenses. It also provides vital liability coverage, so you are protected if you accidentally cause damage to the building or if a guest is injured inside your unit.",
        "cov1": "Replacement Cost for stolen or damaged electronics & furniture",
        "cov2": "Personal Liability shield for accidental property damage",
        "cov3": "Hotel and Temporary Housing stipends",
        "cov4": "Identity Theft and fraud protection riders"
    },
    {
        "filename": "vehicle-insurance.html",
        "title": "Vehicle Insurance",
        "img": "https://images.unsplash.com/photo-1563720360172-67b8f3dce741?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "desc1": "Whether you commute daily or drive for pleasure, navigating the roads inherently carries risks. Our premier Vehicle Insurance policies are built to shield you from the financial fallout of collisions, theft, vandalism, and natural disasters. We work with you to dial in the exact coverage limits and deductibles that match your driving profile and budget.",
        "desc2": "Beyond standard collision and comprehensive coverage, we offer premium additions like 24/7 roadside assistance, rental car reimbursement, and accident forgiveness. At Insurance Package Network, we believe deeply in rewarding safe drivers, offering massive discounts for clean records and bundled auto policies.",
        "cov1": "Collision & Comprehensive physical damage coverage",
        "cov2": "Uninsured and Underinsured Motorist shielding",
        "cov3": "Medical Payments & Personal Injury Protection",
        "cov4": "24/7 Guaranteed Roadside Assistance and Towing"
    },
    {
        "filename": "property-insurance.html",
        "title": "Property Insurance",
        "img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "desc1": "Owning multiple properties or holding real estate investments requires dynamic, specialized protection. Our Property Insurance portfolios safeguard secondary homes, seasonal properties, rental apartments, and vacant properties against catastrophic losses. We cover foundational vulnerabilities that go beyond standard homeowners policies.",
        "desc2": "Our coverage isn't just about repairing physical damage; it actively protects your revenue. Many of our specialized real estate packages include loss of rental income coverage, ensuring that your cash flow remains stable even if a property becomes temporarily uninhabitable after a major incident.",
        "cov1": "Specialized Commercial and Residential structure protection",
        "cov2": "Loss of Rental Income coverage",
        "cov3": "Expanded Commercial Liability protection",
        "cov4": "Multi-Property discounted portfolios"
    },
    {
        "filename": "business-insurance.html",
        "title": "Business Insurance",
        "img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "desc1": "Every successful enterprise needs a robust safety net. Business Insurance from Insurance Package Network encompasses a massive array of commercial protections, including general commercial liability, commercial property damage, and specialized professional liability (Errors and Omissions). We protect your life's work from litigation and total loss.",
        "desc2": "We also offer critical comprehensive policies like Worker's Compensation and Cyber Liability coverage, ensuring that both your employees and your digital assets are shielded from modern threats. Our expert commercial agents will perform a deep dive into your business model to build a bespoke risk mitigation fortress.",
        "cov1": "General Commercial Liability and Property Damage",
        "cov2": "Professional Liability (Errors & Omissions)",
        "cov3": "Workers Compensation and Employee Policies",
        "cov4": "Cyber Data Breach protection"
    },
    {
        "filename": "travel-insurance.html",
        "title": "Travel Insurance",
        "img": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "desc1": "Exploring the world should be exhilarating, not stressful. Travel Insurance offers absolute peace of mind by covering the massive unexpected costs of foreign emergency medical care, sudden trip cancellations, drastic flight delays, and totally lost luggage. We make sure a medical emergency abroad doesn't bankrupt you.",
        "desc2": "Whether you are taking a quick weekend flight or embarking on a global multi-month expedition, Insurance Package Network offers tailored single-trip and annual multi-trip packages. You get 24/7 access to our global emergency hotline, connecting you instantly to doctors, translators, and logistical support anywhere on Earth.",
        "cov1": "Emergency Medical Evacuation Healthcare",
        "cov2": "Trip Cancellation and Interruption reimbursement",
        "cov3": "Baggage Loss and Personal Item Replacement",
        "cov4": "24/7 Global Concierge and Support Hotline"
    }
]

for p in pages:
    content = template.replace('TITLE_VAR', p['title'])
    content = content.replace('IMG_VAR', p['img'])
    content = content.replace('DESC_1_VAR', p['desc1'])
    content = content.replace('DESC_2_VAR', p['desc2'])
    content = content.replace('COV_1_VAR', p['cov1'])
    content = content.replace('COV_2_VAR', p['cov2'])
    content = content.replace('COV_3_VAR', p['cov3'])
    content = content.replace('COV_4_VAR', p['cov4'])
    
    filepath = os.path.join("e:\\Insurance Websites", p['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully generated all 6 pages!")
