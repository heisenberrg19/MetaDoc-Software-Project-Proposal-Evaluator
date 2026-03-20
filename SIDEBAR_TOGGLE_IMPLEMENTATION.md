# Sidebar Toggle Feature - Implementation Guide

## Overview
A reusable sidebar hide/show feature has been implemented across all dashboard pages:
- **Overview** (`/dashboard`)
- **Deliverables** (`/dashboard/deliverables`)
- **Class Record** (`/dashboard/class-record`)
- **Reports** (`/dashboard/reports`)

## Components & Files

### 1. **DashboardLayout.jsx** (Updated)
- Central management of sidebar hidden state
- Shared across all special pages
- Toggle button in topbar (only visible on special pages)
- Mini-navbar with:
  - Navigation icons for all 4 pages
  - Team 7 button (footer)
  - Logout button (footer)

### 2. **Reusable Hook: useSidebarHidden.js** (NEW)
**Location:** `src/hooks/useSidebarHidden.js`

```javascript
import { useSidebarHidden } from '../../hooks/useSidebarHidden';

const { 
  sidebarHidden,      // Current state (boolean)
  setSidebarHidden,   // State setter
  isSpecialPage,      // Is current page supported (boolean)
  toggleSidebar       // Callback function to toggle
} = useSidebarHidden();
```

### 3. **CSS Updates: DashboardLayout.css**
New classes added:
- `.mini-navbar` - Fixed 80px sidebar containing icons
- `.mini-nav-items` - Container for navigation items
- `.mini-nav-item` - Individual navigation icon
- `.mini-nav-item-active` - Active navigation state (gold)
- `.mini-nav-footer` - Footer section with Team 7 & Logout
- `.mini-nav-footer-item` - Footer button styling
- `.mini-nav-logout:hover` - Special red hover for logout
- `.dashboard-layout.sidebar-hidden-reports` - Hidden state class

## Features

### ✅ Automatic Page Detection
Sidebar toggle is **automatically available** on:
- Overview page
- Deliverables page
- Class Record page
- Reports page

### ✅ Icon-Only Navigation
When sidebar is hidden, users see:
- 80px wide navbar on the left
- Icons only (no text)
- Tooltips on hover showing page names
- Gold highlight for active page

### ✅ Footer Controls
Mini-navbar footer includes:
- **Team 7** (Code2 icon) - Opens team modal
- **Logout** (LogOut icon) - Logs user out

### ✅ State Persistence
- Sidebar state saved to localStorage as `sidebar-hidden-all-pages`
- State persists across page refreshes and navigation

### ✅ Smooth Transitions
- Hover effects on all icons
- 0.2s ease transitions
- Scale effects on active state
- Special styling for logout button

## Usage

### In DashboardLayout (Already Implemented)
The toggle button appears automatically in the topbar when on special pages:
```jsx
{isSpecialPage && (
  <button
    className="topbar-sidebar-toggle"
    onClick={toggleSidebar}
    title={sidebarHidden ? 'Show Sidebar' : 'Hide Sidebar'}
  >
    {sidebarHidden ? <Menu size={20} /> : <ChevronLeft size={20} />}
  </button>
)}
```

### Using the Hook in Other Components
If you need to use this feature elsewhere:
```javascript
import { useSidebarHidden } from '../hooks/useSidebarHidden';

export function MyComponent() {
  const { sidebarHidden, isSpecialPage, toggleSidebar } = useSidebarHidden();
  
  if (!isSpecialPage) return null;
  
  return (
    <button onClick={toggleSidebar}>
      {sidebarHidden ? 'Show' : 'Hide'} Sidebar
    </button>
  );
}
```

## Visual Design
- **Colors:** Maroon gradient background matching main sidebar
- **Width:** 80px (compact, icon-based)
- **Icon Size:** 20px
- **Hover State:** 10% white background
- **Active State:** Gold background with maroon text (matching main nav)
- **Footer Border:** Subtle line separating main nav from footer

## File Structure
```
frontend/metadoc/src/
├── hooks/
│   └── useSidebarHidden.js (NEW - Reusable hook)
├── components/
│   └── Layout/
│       └── DashboardLayout.jsx (Updated with mini-navbar)
├── styles/
│   └── DashboardLayout.css (Updated with mini-navbar styles)
├── pages/
│   ├── Dashboard.jsx
│   ├── Deliverable.jsx
│   ├── ClassRecord.jsx
│   └── Reports.jsx
```

## Browser Compatibility
- Works on all modern browsers
- localStorage support required
- CSS Grid and Flexbox support required

## Future Enhancements
- Dark mode support for mini-navbar
- Keyboard shortcuts for toggle
- Animation preferences (prefers-reduced-motion)
- Mobile-specific handling
