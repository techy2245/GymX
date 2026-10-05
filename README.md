# GymX

GymX is an independent, open-source mobile fitness and nutrition platform. Built upon the robust foundation of OpenGym, GymX is engineered to be the ultimate, all-in-one health companion. It eliminates the need for multiple apps by deeply integrating workout tracking, an embedded music player, AI-powered nutrition, and cloud-synchronized lifestyle management into a single cohesive interface.

## The Vision

Most individuals constantly switch between a fitness tracker for lifting, a nutrition app for food logging, and a media app for music. GymX unifies this entire ecosystem. Your workout data, diet tracking, lifestyle metrics, and audio are entirely controlled within one application, with the added security of cloud backups to keep your progress safe across devices.

## Comprehensive Feature Set

### 1. Advanced Workout & Progression Tracking
* **Comprehensive Exercise Logging:** Track distinct exercises, sets, reps, and precise weight increments.
* **Routine Management:** Build and save custom daily routines for quick access.
* **Performance Analytics:** Automatically monitor Personal Records (PRs), total volume lifted, and historical workout data.

### 2. AI-Powered Nutrition & Diet Logging
* **Smart Food Scanner:** Use the device camera to scan meals or barcodes, utilizing integrated AI to automatically calculate calories and macronutrients (proteins, carbs, fats).
* **Predictive Weight Modeling:** Input daily food habits to generate data-driven forecasts showing projected weight gain or loss over time based on caloric surplus or deficit.
* **Manual Food Logging:** A comprehensive, searchable database for manual entry of meals, snacks, and custom recipes.

### 3. Lifestyle & Recovery Tracking
* **Hydration Monitoring:** A built-in daily water tracker with customizable intake goals and easy-log shortcuts.
* **Sleep Analytics:** Log sleep duration and quality to correlate recovery metrics with gym performance and weight trends.

### 4. Integrated Audio Engine
* **In-App Media Player:** A functional music player embedded within the workout screen, featuring media controls without needing to minimize the app.
* **Smart Routine Automation:** Bind specific local or licensed playlists to specific workout routines (e.g., triggering a high-energy playlist automatically on deadlift days).

### 5. Account Management & Cloud Synchronization
* **Secure Authentication:** Users can create personalized accounts and log in using standard credentials to secure their profiles.
* **Cloud Data Backup:** All tracked data—including workouts, nutrition logs, sleep metrics, and hydration history—is automatically synced and saved to the cloud.
* **Cross-Device Access:** Seamlessly access your fitness and nutrition ecosystem from any authenticated device without losing progress.
* **Offline-Capable Engine:** Core logging features remain functional without an internet connection, caching data locally and syncing automatically once a connection is restored.

## Current Development Phase

**Current Focus: Environment Setup, Codebase Mapping, and Architecture Restructuring**

We are currently reverse-engineering the OpenGym repository and preparing the foundation for the GymX feature set. Active development tasks include:
* Systematically mapping the OpenGym codebase to understand existing UI component hierarchies and state management flows.
* Integrating a secure authentication and cloud database solution (e.g., Firebase or Supabase) to handle user accounts and data synchronization.
* Researching lightweight, on-device AI models for food scanning and macro calculation.
* Designing the schema for the new database to support the expanded nutrition, sleep, and hydration metrics.

## Acknowledgments & Credits

This project was heavily inspired by and built upon the open-source foundation of [OpenGym](https://github.com/arvids-unavailable/openGym). We are incredibly grateful to the original developers for providing a robust starting point that allowed us to build out our custom fitness, nutrition, and audio integration features.

## Tech Stack

* **Platform:** Mobile (Framework inherited from OpenGym codebase)
* **Backend & Database:** Cloud Synchronization & Auth (e.g., Firebase/Supabase/Custom Backend)
* **AI Engine:** Machine learning integrations for food recognition (Implementation pending)
* **Workflow:** Git / GitHub

## License

This project is strictly licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). See the `LICENSE` file for full details and distribution requirements.
