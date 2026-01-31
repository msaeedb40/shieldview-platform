import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink, Router } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  template: `
    <div class="auth-wrapper">
      <div class="glass-panel auth-card">
        <h1>Join ShieldView</h1>
        <p class="subtitle">Start your proactive security journey</p>
        
        <form (submit)="onSubmit($event)">
          <input type="text" name="username" [(ngModel)]="user.username" placeholder="Username" required>
          <input type="email" name="email" [(ngModel)]="user.email" placeholder="Email Address" required>
          <input type="password" name="password" [(ngModel)]="user.password" placeholder="Password" required>
          
          <button type="submit" class="btn-primary w-full" [disabled]="loading">
            {{ loading ? 'CREATING ACCOUNT...' : 'REGISTER' }}
          </button>
        </form>
        
        <div class="auth-footer">
          <span>Already have an account?</span>
          <a routerLink="/login">Sign In</a>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .auth-wrapper {
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at top right, #1a1a1a, #050505);
    }
    .auth-card { width: 400px; text-align: center; }
    h1 {
      margin: 0;
      font-size: 2.2rem;
      background: linear-gradient(45deg, #00f2ff, #7000ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .subtitle { color: #888; margin-bottom: 2rem; }
    .auth-footer { margin-top: 1.5rem; font-size: 0.9rem; color: #aaa; }
    .auth-footer a { color: #00f2ff; text-decoration: none; margin-left: 0.5rem; }
    .w-full { width: 100%; }
  `]
})
export class RegisterComponent {
  private authService = inject(AuthService);
  private router = inject(Router);
  user = { username: '', email: '', password: '' };
  loading = false;

  onSubmit(e: Event) {
    e.preventDefault();
    this.loading = true;
    this.authService.register(this.user).subscribe({
      next: () => {
        alert("Account created successfully. Please login.");
        this.router.navigate(['/login']);
        this.loading = false;
      },
      error: () => {
        alert("Registration failed.");
        this.loading = false;
      }
    });
  }
}
