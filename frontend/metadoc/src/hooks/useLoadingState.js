import { useState, useEffect } from 'react';

/**
 * Custom hook to manage dynamic loading states.
 * Returns { showLongLoading } which becomes true after the specified delay if loading is active.
 * 
 * @param {boolean} loading - Current loading state from the component.
 * @param {number} delay - Delay in ms before switching to long loading UI (default 3000ms).
 */
export const useLoadingState = (loading, delay = 3000) => {
  const [showLongLoading, setShowLongLoading] = useState(false);

  useEffect(() => {
    let timer;
    if (loading) {
      timer = setTimeout(() => {
        setShowLongLoading(true);
      }, delay);
    } else {
      setShowLongLoading(false);
    }

    return () => {
      if (timer) clearTimeout(timer);
    };
  }, [loading, delay]);

  return { showLongLoading };
};
